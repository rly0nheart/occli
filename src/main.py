#!/usr/bin/env python3

import logging
import argparse
import requests
from datetime import datetime
from lib.colors import red,white,green,reset

class occli:
	def __init__(self,args):
		self.api = f"https://api.opencorporates.com/v0.4.8/companies/search?q={args.query}*"
		if args.query:
		    self.search()
		elif args.licence:
			exit(self.licence())
		else:
		    exit(f"{white}occli: use {green}-h{white} or {green}--help{white} to show help message.{reset}")
		
	    	
	# searching compan(y)(ies) on OpenCorporates    	
	def search(self):
		interval = 0
		response = requests.get(self.api).json()
		if response['results']['companies'] == []:
			logging.info(f"{white}No results found for {args.query}. Try a different search or try again later.{reset}")
		else:
			for number in range(interval, int(response['results']['per_page'])+1):
				interval += 1
				data = {"Company No#": response['results']['companies'][number]['company']['company_number'],
			                 "Jurisdiction code": response['results']['companies'][number]['company']['jurisdiction_code'],
			                 "Incorporation date": response['results']['companies'][number]['company']['incorporation_date'],
    			             "Dissolution date": response['results']['companies'][number]['company']['dissolution_date'],
			                 "Company type": response['results']['companies'][number]['company']['company_type'],
			                 "Registry URI": response['results']['companies'][number]['company']['registry_url'],
			                 "Branch": response['results']['companies'][number]['company']['branch'],
    			             "Branch status": response['results']['companies'][number]['company']['branch_status'],
    			             "Is inactive?": response['results']['companies'][number]['company']['inactive'],
    			             "Current status": response['results']['companies'][number]['company']['current_status'],
			                 "Created at": response['results']['companies'][number]['company']['created_at'],
			                 "Updated at": response['results']['companies'][number]['company']['updated_at'],
			                 "Previous name(s)": response['results']['companies'][number]['company']['previous_names'],
			                 "Registered address": response['results']['companies'][number]['company']['registered_address'],
    			             "Address in full": response['results']['companies'][number]['company']['registered_address_in_full'],
			                 "Industry code(s)": response['results']['companies'][number]['company']['industry_codes'],
			                 "Restricted for marketing": response['results']['companies'][number]['company']['restricted_for_marketing'],
			                 "Native company No#": response['results']['companies'][number]['company']['native_company_number'],
			                 "OpenCorporates URI": response['results']['companies'][number]['company']['opencorporates_url']
				}
				print(f"\n\n{white}{response['results']['companies'][number]['company']['name']}{reset}")
				for key, value in data.items():
					print(f"{white} ├─ {key}: {green}{value}{reset}")
					
				if args.dump:
				   print(self.write(data,number,response))
				   
				if number == int(response['results']['per_page'])-1:
					break			
			
			
	# Writing results to a file
	def write(self,data,number,response):
	    with open(args.dump, 'a') as file:
	        file.write(f"\n\n{response['results']['companies'][number]['company']['name']}\n")
	        for key, value in data.items():
	        	file.write(f" ├─ {key}: {value}\n")
	        file.close()
	        
	    if args.verbose:
	    	logging.info(f'{white}Output written to {green}{args.dump}{reset}')
	    	
	    	
	def licence(self):
	    with open('LICENSE','r') as file:
	    	content = file.read()
	    	file.close()
	    return content
	    	

# Parsing command line arguments
parser = argparse.ArgumentParser(description=f"{white}OpenCorporates Command Line Interface [{red}Unofficial{white}]{reset}",epilog=f"{green}OpenCorporates.com{white} is a website that shares data on corporations under the copyleft Open Database License. Developed by {green}Richard Mwewa{white} | https://about.me/{green}rly0nheart{reset}")
parser.add_argument('-q','--query',metavar=f'{white}company-name{reset}')
parser.add_argument("-d","--dump",help=f"{white}dump output to a specified file{reset}",metavar=f"{white}path/to/file{reset}")
parser.add_argument("-v","--verbose",help=f"{white}run occli in verbose mode{reset}",action="store_true")
parser.add_argument("--version",version=f"{white}v0.3.4 Released on 16th February 2022 {reset}",action="version")
parser.add_argument('--licence','--license',help=f'show program\'s licen(cs)e and exit',action='store_true')
args = parser.parse_args()

start_time = datetime.now()
if args.verbose:
	logging.basicConfig(format=f'{white}* %(message)s{reset}',level=logging.DEBUG)
