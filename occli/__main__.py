#!/usr/bin/env python3

import sys
import json
import logging
import argparse
import requests
from pprint import pprint
from datetime import datetime

# Colors will not be diplayed on windows or macOS machines
colors = True
platf = sys.platform
if platf.lower().startswith(("os", "win", "darwin","ios")): 
    colors = False

if not colors:
	green = red = white = reset = ""

else:                                                 
    white = "\033[97m"
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"


def occli():
	start = datetime.now()
	api = f"https://api.opencorporates.com/v0.4.8/"
	parser = argparse.ArgumentParser(description=f"{green}Unofficial Open Corporates client:  {white}OpenCorporates is a website that shares data on corporations under the copyleft Open Database License. This is an unofficial open corporates command line client developed by {white}Richard Mwewa | {red}https://github.com/{white}rlyonheart{reset}")
	parser.add_argument("-c", "--company",help=f"{white}company name{reset}", dest="companyname", metavar=f"{white}COMPANYNAME{reset}")
	parser.add_argument("--versions",help=f"{white}show API version information{reset}", dest="versions", action="store_true")
	parser.add_argument("-o","--output",help=f"{white}write output to a  {green}file{reset}",dest="output", metavar="FILENAME")
	parser.add_argument("-r","--raw",help=f"{white}return results in {green}raw{white} json{reset}",dest="raw", action="store_true")
	parser.add_argument("-v","--verbose",help=f"{white}verbosity{reset}",dest="verbose", action="store_true")
	args = parser.parse_args()
	if args.verbose:
	    logging.basicConfig(format=f"{white}%(message)s{reset}",level=logging.DEBUG)

	
	if args.companyname:
		companies(args,api,start)
	elif args.versions:
		versions(args,api)
	else:
		print(f"""{white}usage: occli [{green}-h{white}] [{green}-c {white}COMPANYNAME] [{green}--versions{white}] [{green}-o {white}FILENAME] [{green}-r{white}] [{green}-v{white}]

optional arguments:
  {green}-h{white}, {green}--help{white}            show this help message and {red}exit{green}
  
  -c {white}COMPANYNAME, {green}--company{white} COMPANYNAME
                        company name
                        
  {green}--versions{white}            show API version
                        information
                        
  {green}-o {white}FILENAME, {green}--outfile {white}FILENAME
                        write output to a
                        file
                        
  {green}-r{white}, {green}--raw{white}             return results in
                        raw json
                        
  {green}-v{white}, {green}--verbose{white}         run occli in verbose mode{reset}""")


def companies(args,api,start):
	api = api+f"companies/search?q={args.companyname}*"	    
	interval = 0
	retries = 0
	# Main loop
	while True:
		retries += 1
		try:
			response = requests.get(api).json()
			for number in range(interval, int(response['results']['per_page'])+1):
				interval += 1
				results = (f"""

{white}{response['results']['companies'][number]['company']['name']}
├ Company Number: {green}{response['results']['companies'][number]['company']['company_number']}{white}
├─ Jurisdiction Code: {green}{response['results']['companies'][number]['company']['jurisdiction_code']}{white}
├── Incoporation Date: {green}{response['results']['companies'][number]['company']['incorporation_date']}{white}
├─ Dissolution Date: {green}{response['results']['companies'][number]['company']['dissolution_date']}{white}
├─── Company Type: {green}{response['results']['companies'][number]['company']['company_type']}{white}
├─ Registry URL: {green}{response['results']['companies'][number]['company']['registry_url']}{white}
├ Branch: {green}{response['results']['companies'][number]['company']['branch']}{white}
├ Branch Status: {green}{response['results']['companies'][number]['company']['branch_status']}{white}
├─ Inactive: {green}{response['results']['companies'][number]['company']['inactive']}{white}
├─ Current Status: {green}{response['results']['companies'][number]['company']['current_status']}{white}
├─ Created On: {green}{response['results']['companies'][number]['company']['created_at']}{white}
├─── Updated On: {green}{response['results']['companies'][number]['company']['updated_at']}{white}
├─ Previous Names: {green}{response['results']['companies'][number]['company']['previous_names']}{white}
├── Information Source | Publisher: {green}{response['results']['companies'][number]['company']['source']['publisher']}{white}  | URL: {green}{response['results']['companies'][number]['company']['source']['url']}{white}  | Retrieved On: {green}{response['results']['companies'][number]['company']['source']['retrieved_at']}{white}
├ Registered Address: {green}{response['results']['companies'][number]['company']['registered_address']}{white}
├ Address In Full: {green}{response['results']['companies'][number]['company']['registered_address_in_full']}{white}
├── Industry Codes: {green}{response['results']['companies'][number]['company']['industry_codes']}{white}
├─ Restricted For Marketing: {green}{response['results']['companies'][number]['company']['restricted_for_marketing']}{white}
├ Native Company Number: {green}{response['results']['companies'][number]['company']['native_company_number']}{white}
└╼ Open Corporates URL: {red}{response['results']['companies'][number]['company']['opencorporates_url']}{reset}
""")
				if args.raw:
				    raw(args,results,response)
				    break
				  
				else:
				    print(results)
				    if args.output:
				    	output(args,results,response)
				    	
				if number == int(response['results']['per_page'])-1:
					break
			
			if args.verbose:
				exit(f"{white}[{green}•{white}] Occli stopped in {red}{datetime.now()-start}{white} seconds.{reset}\n")
				
		except IndexError:
			if args.verbose:
				exit(f"{white}[{red}!{white}] Company: ({red}{args.corporation}{white}) {red}Not Found{white}.{reset}\n")
			break
			
		except KeyboardInterrupt:
			if args.verbose:
				exit(f"\n{white}[{red}x{white}] Occli interrupted ({red}Ctrl{white}+{red}C{white}).{reset}\n")
			exit()
			
		except Exception as e:
			if args.verbose:
				print(f"\n{white}[{red}!{white}] Error ({red}{args.companyname}{white}): {red}{e}{reset}")
				print(f"{white}[{green}*{white}] Retrying::attempt({retries})...{reset}")

	
			
# Save results
# If the raw flag is included, results will not only be returned in json format but will also be written in json
def output(args,results,response):
    if args.raw:
    	object = json.dumps(response, indent=4)
    	with open(args.output, "a") as raw:
    		raw.write(object)
    		raw.close()
    		
    else:
        with open(args.output, "a") as file:
        	file.write(results)
        	file.close()
        	
    if args.verbose:
        print(f"\n{white}[{green}✓{white}] Results written to ./{green}{args.output}{reset}")
        
        
# Return results in raw json format    
def raw(args,results,response):
    print("\n")
    pprint(response)
    if args.output:
        output(args,results,response)
        
        
def versions(args,api):
    api = api+"versions"
    get_ver = requests.get(api).json()
    versions = f"""{white}
Open Corporates API Version Information
├ current version: {green}{get_ver['results']['versions']['current_version']}{white}
├─ requested version : {green}{get_ver['results']['versions']['requested_version']}{white}
├ supported versions: {green}{get_ver['results']['versions']['supported_versions']}{reset}
"""
    if args.raw:
        pprint(get_ver)      
    else:
        print(versions)
        
 		
if __name__ == "__main__":
	occli()
