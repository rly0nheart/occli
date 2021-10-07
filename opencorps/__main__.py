#!/usr/bin/env python3

import json
import logging
import random
import argparse
import requests
from pprint import pprint
from datetime import datetime
from resources.headers import user_agents
from assets.colors import red,green,white,reset

class OpenCorporates:
	def __init__(self,args):
		self.api = f"https://api.opencorporates.com/v0.4.1/companies/search?q={args.corporation}*"
		self.headers = {"User-Agent": f"{random.choice(user_agents)}"}
		self.response = requests.get(self.api, headers=self.headers).json()
		
	def on_connection(self):
		interval = 0
		for number in range(interval, int(self.response['results']['per_page'])+1):
			interval += 1
			results = (f"""

{white}{self.response['results']['companies'][number]['company']['name']}
├ Company Number: {green}{self.response['results']['companies'][number]['company']['company_number']}{white}
├─ Jurisdiction Code: {green}{self.response['results']['companies'][number]['company']['jurisdiction_code']}{white}
├── Incoporation Date: {green}{self.response['results']['companies'][number]['company']['incorporation_date']}{white}
├─ Dissolution Date: {green}{self.response['results']['companies'][number]['company']['dissolution_date']}{white}
├─── Company Type: {green}{self.response['results']['companies'][number]['company']['company_type']}{white}
├─ Registry URL: {green}{self.response['results']['companies'][number]['company']['registry_url']}{white}
├ Branch: {green}{self.response['results']['companies'][number]['company']['branch']}{white}
├ Branch Status: {green}{self.response['results']['companies'][number]['company']['branch_status']}{white}
├─ Inactive: {green}{self.response['results']['companies'][number]['company']['inactive']}{white}
├─ Current Status: {green}{self.response['results']['companies'][number]['company']['current_status']}{white}
├─ Created On: {green}{self.response['results']['companies'][number]['company']['created_at']}{white}
├─── Updated On: {green}{self.response['results']['companies'][number]['company']['updated_at']}{white}
├─ Previous Names: {green}{self.response['results']['companies'][number]['company']['previous_names']}{white}
├── Information Source | Publisher: {green}{self.response['results']['companies'][number]['company']['source']['publisher']}{white}  | URL: {green}{self.response['results']['companies'][number]['company']['source']['url']}{white}  | Retrieved On: {green}{self.response['results']['companies'][number]['company']['source']['retrieved_at']}{white}
├ Registered Address: {green}{self.response['results']['companies'][number]['company']['registered_address']}{white}
├ Address In Full: {green}{self.response['results']['companies'][number]['company']['registered_address_in_full']}{white}
├── Industry Codes: {green}{self.response['results']['companies'][number]['company']['industry_codes']}{white}
├─ Restricted For Marketing: {green}{self.response['results']['companies'][number]['company']['restricted_for_marketing']}{white}
├ Native Company Number: {green}{self.response['results']['companies'][number]['company']['native_company_number']}{white}
└╼ Open Corporates URL: {red}{self.response['results']['companies'][number]['company']['opencorporates_url']}{reset}
""")
			if args.raw:
			 print("\n")
			 pprint(self.response)
			 if args.output:
			 	self.raw_output()
			 break
			 		
			else:
				print(results)
				if args.output:
					self.output(results)
					
			if number == int(self.response['results']['per_page'])-1:
				break
			
	
	def output(self,results):
	    with open(args.output, "a") as file:
	    	file.write(results)
	    	file.close()
	   
	def raw_output(self):
	    object = json.dumps(self.response, indent=4)
	    with open(args.output, "a") as file:
	    	file.write(object)
	    	file.close()
    		


parser = argparse.ArgumentParser(description=f"{green}Unofficial Open Corporates CLI:  {white}OpenCorporates is a website that shares data on corporations under the copyleft Open Database License. This is an unofficial open corporates command line tool developed by {white}Richard Mwewa | {red}https://github.com/{white}rlyonheart{reset}")
parser.add_argument("corporation", help=f"{white}company name{reset}")
parser.add_argument("-o","--outfile",help=f"{white}write output to a  {green}file{reset}",dest="output", metavar="FILENAME")
parser.add_argument("-r","--raw",help=f"{white}return results in {green}raw{white} json{reset}",dest="raw", action="store_true")
parser.add_argument("-v","--verbose",help=f"{white}verbosity{reset}",dest="verbose", action="store_true")
args = parser.parse_args()
 		
if __name__ == "__main__":
	start = datetime.now()
	mode = ""
	if args.raw:
		mode = f"{white}* Started  at {red}{start}{white} (query: {green}{args.corporation}{white}) (raw_mode: {green}active{white})...{reset}"
	else:
		mode = f"{white}* Started  at {red}{start}{white} (query: {green}{args.corporation}{white}) (raw_mode: {red}inactive{white})...{reset}"
		
	if args.verbose:
	    print(mode, end="")
	    logging.basicConfig(format=f"{white}%(message)s{reset}",level=logging.DEBUG)
	    
	while True:
		try:
			OpenCorporates(args).on_connection()
			if args.verbose:
				exit(f"{white}* Stopped in {red}{datetime.now()-start}{white} seconds.{reset}\n")
			break
			
		except IndexError:
			if args.verbose:
				exit(f"{white}* Corporation: ({red}{args.corporation}{white}) {red}Not Found{white}.{reset}\n")
			break
			
		except KeyboardInterrupt:
			if args.verbose:
				exit(f"\n{white}* Process interrupted ({red}Ctrl{white}+{red}C{white}).{reset}\n")
			exit()
			
		except Exception as e:
			if args.verbose:
				print(f"\n{white}* Error ({red}{args.corporation}{white}): {red}{e}{reset}")
				print(f"{white}* Retrying ({green}{args.corporation}{white})...{reset}")
