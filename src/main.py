#!/usr/bin/env python3

import logging
import argparse
import requests
from datetime import datetime
from lib.colors import red,white,green,reset

class occli:
	def __init__(self,args):
		self.api = f"https://api.opencorporates.com/v0.4.8/companies/search?q={args.search}*"		
			
	def on_connection(self):
	    if args.search:
	    	self.search()
	    else:
	    	exit(f"{white}occli: try {green}occli --h{white} or {green}occli --help{white} to view help message{reset}")
	    	
	# searching compan(y)(ies) on OpenCorporates    	
	def search(self):	    
		interval = 0
		response = requests.get(self.api).json()
		if response['results']['companies'] == []:
			print(f"{white}[{red}^{white}] No results found for {args.search}. Try a different search or try again later.{reset}")
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
					
				if args.output:
				   print(self.write(data,number,response))
				   
				if number == int(response['results']['per_page'])-1:
					break
				
			
			
	# Writing results to a file
	def write(self,data,number,response):
	    with open(args.output, "a") as file:
	        file.write(f"\n\n{response['results']['companies'][number]['company']['name']}\n")
	        for key, value in data.items():
	        	file.write(f" ├─ {key}: {value}\n")
	        file.close()
	        
	    if args.verbose:
	    	return f"\n{white}[{green}+{white}] Output written to ./{green}{args.output}{reset}"
	    	

parser = argparse.ArgumentParser(description=f"{white}Unofficial Command Line Interface for OpenCorporates{reset}",epilog=f"{white}OpenCorporates.com is a website that shares data on corporations under the copyleft Open Database License. Developed by {green}Richard Mwewa{white} | https://about.me/{green}rly0nheart{reset}")
parser.add_argument("search",help=f"{white}company name{reset}")
parser.add_argument("-o","--output",help=f"{white}write output to a file{reset}",metavar=f"{white}path/to/file{reset}")
parser.add_argument("-v","--verbose",help=f"{white}run occli in verbose mode (recommended){reset}",dest="verbose", action="store_true")
parser.add_argument("--version",version=f"{white}v0.3.2 Released at 12:40AM CAT 2022-01-22 {reset}",action="version")
args = parser.parse_args()
start_time = datetime.now()
if args.verbose:
	logging.basicConfig(format=f"{white}[{green}~{white}] %(message)s{reset}",level=logging.DEBUG)
