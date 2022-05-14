#!/usr/bin/env python3

import logging
import argparse
import requests
from tqdm import tqdm
from lib.misc import Banner
from datetime import datetime

class Attributes:
    positive = "[ + ]"
    negative = "[ - ]"
    warning = "[ ! ]"
    error = "[ x ]"
    info = "[ * ]"
    prompt = "[ ? ]"
    
    
class Occli:
	def __init__(self,args):
	    self.api = f"https://api.opencorporates.com/v0.4.8/companies/search?q={args.query}*"
	    if args.query:
	        self.search()
	    elif args.update:
	        self.check_update()
	    else:
	    	exit(f"occli: use -h or --help to show help message.")	   
		
	    	
	# searching compan(y)(ies) on OpenCorporates    	
	def search(self):
		interval = 0
		response = requests.get(self.api).json()
		if response['results']['companies'] == []:
			print(f"{Attributes.negative} No results found for query ({args.query}). Try a different search or try again later.")
		else:
			for number in range(interval, int(response['results']['per_page'])+1):
				interval += 1
				data = {"Company No#": response['results']['companies'][number]['company']['company_number'],
			                 "Branch": response['results']['companies'][number]['company']['branch'],
    			             "Branch status": response['results']['companies'][number]['company']['branch_status'],
    			             "Current status": response['results']['companies'][number]['company']['current_status'],
			                 "Previous name(s)": response['results']['companies'][number]['company']['previous_names'],
			                 "Registered address": response['results']['companies'][number]['company']['registered_address'],
    			             "Address in full": response['results']['companies'][number]['company']['registered_address_in_full'],
			                 "Industry code(s)": response['results']['companies'][number]['company']['industry_codes'],
			                 "Restricted for marketing": response['results']['companies'][number]['company']['restricted_for_marketing'],
			                 "Native company No#": response['results']['companies'][number]['company']['native_company_number'],
			                 "Company type": response['results']['companies'][number]['company']['company_type'],
			                 "Jurisdiction code": response['results']['companies'][number]['company']['jurisdiction_code'],
			                 "Incorporation date": response['results']['companies'][number]['company']['incorporation_date'],
    			             "Dissolution date": response['results']['companies'][number]['company']['dissolution_date'],
			                 "Registry URI": response['results']['companies'][number]['company']['registry_url'],
			                 "Is inactive?": response['results']['companies'][number]['company']['inactive'],
    			             "Created at": response['results']['companies'][number]['company']['created_at'],
			                 "Updated at": response['results']['companies'][number]['company']['updated_at'],
			                 "OpenCorporates URI": response['results']['companies'][number]['company']['opencorporates_url']
				}
				print(f"\n{response['results']['companies'][number]['company']['name']}")
				for key, value in data.items():
					print(f"├─ {key}: {value}")
				print("\n")
					
				if args.output:
				   print(self.write(data,number,response))
				   
				if number == int(response['results']['per_page'])-1:
					break			
			
			
	# Writing results to a file
	def write(self,data,number,response):
	    with open(args.output, 'a') as file:
	        file.write(f"\n\n{response['results']['companies'][number]['company']['name']}\n")
	        for key, value in data.items():
	        	file.write(f" ├─ {key}: {value}\n")
	        file.close()
	        
	    print(f"{Attributes.positive} Output written to ./{args.output}")
	    	
	    	
	def check_update(self):
	    response = requests.get("https://api.github.com/repos/rly0nheart/occli/releases/latest")
	    if response.json()['tag_name'] == Banner.version:
	        print(f"{Attributes.info} Occli is up to date. Check again soon :)")
	    else:
	    	while True:
	    	    print(f"{Attributes.info} A new release is available ({response.json()['tag_name']})")
	    	    prompt = input(f"{Attributes.prompt} Would you like to get it? (y/n) ")
	    	    if prompt == "y":
	    	        files_to_update = ['src/main.py','lib/misc.py','occli','.github/dependabot.yml','.github/ISSUE_TEMPLATE/bug_report.md','.github/ISSUE_TEMPLATE/feature_request.md','.github/ISSUE_TEMPLATE/config.yml','LICENSE','README.md','requirements.txt']
	    	        for file in tqdm(files_to_update,desc='[ * ] Updating'):
	    	            data = requests.get(f'https://raw.githubusercontent.com/rly0nheart/occli/master/{file}')
	    	            with open(file, 'wb') as code:
	    	                code.write(data.content)
	    	                code.close()
	    	        print(f"{Attributes.positive} Updated successfully. Re-run program.")
	    	        break
	    	        
	    	    elif prompt == "n":
	    	        print(f"{Attributes.info} Update skipped. Re-run program.")
	    	        break
	    	    else:
	    	    	print(f"\n{Attributes.warning} You entered an invalid response ({prompt}) (expected y or n)")
	    	

# Parsing command line arguments
parser = argparse.ArgumentParser(description=f"Occli — by Richard Mwewa | https://about.me/rly0nheart",epilog=f"Occli is an open-source command line interface for the Open Corporates Database that searches and gets data on corporations under the copyleft Open Database License.")
parser.add_argument('-q','--query',metavar="query")
parser.add_argument("-o","--output",help=f"write output to a specified file",metavar=f"path/to/file")
parser.add_argument("-u","--update",help="check for updates",action="store_true")
parser.add_argument("-d","--debug",help="show network debug information",action="store_true")
parser.add_argument("--version",version=f"v{Banner.version} Released on 16th February 2022 ",action="version")
args = parser.parse_args()
start_time = datetime.now()
if args.debug:
    logging.basicConfig(format=f'{Attributes.info} %(message)s',level=logging.DEBUG)
