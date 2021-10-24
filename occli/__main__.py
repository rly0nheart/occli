#!/usr/bin/env python3

import sys
import json
import logging
import argparse
import requests
from pprint import pprint
from datetime import datetime
from lib.colors import red,white,green,reset


def occli():
	global args
	api = f"https://api.opencorporates.com/v0.4.8/"
	parser = argparse.ArgumentParser(description=f"{white}Unofficial Open Corporates Command Line Client:  {green}Open Corporates{white} is a website that shares data on corporations under the copyleft Open Database License. This is an unofficial open corporates command line client developed by {white}Richard Mwewa | {green}https://github.com/{white}rlyonheart{reset}")
	parser.add_argument("-c", "--company",help=f"{white}company name{reset}", dest="companyname", metavar=f"{white}COMPANYNAME{reset}")
	parser.add_argument("-n", "--company-number", help=f"{white}company number{reset}", dest="companynumber", metavar=f"{white}COMPANYNUMBER{reset}")
	parser.add_argument("-j", "--jurisdiction-code", help=f"{white}jurisdiction {green}code{reset}", dest="jurisdiction", metavar=f"{white}JURISDICTIONCODE{reset}")
	parser.add_argument("--versions",help=f"{white}get latest Open Corporates API version information({green}can also be run in verbose mode{white}){reset}", dest="versions", action="store_true")
	parser.add_argument("-o","--output",help=f"{white}write output to a  {green}file{reset}",dest="output", metavar=f"{white}FILENAME{reset}")
	parser.add_argument("-r","--raw",help=f"{white}return results in raw {green}json{white} format{reset}",dest="raw", action="store_true")
	parser.add_argument("-v","--verbose",help=f"{white}run occli in {green}verbose{white} mode{reset}",dest="verbose", action="store_true")
	args = parser.parse_args()
	if args.verbose:
	    logging.basicConfig(format=f"{white}%(message)s{reset}",level=logging.DEBUG)

	
	if args.companyname:
		companies(args,api)
	elif args.companynumber:
		company_number(args,api)
	elif args.versions:
		versions(args,api)
	else:
		exit(f"{white}occli: try {green}occli --h{white} or {green}occli --help{white} to view help message{reset}")


def companies(args,api):
	api = api+f"companies/search?q={args.companyname}*"	    
	interval = 0
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
		    exit()
		else:
			print(results)
			if args.output:
			    output(args,results,response)
				    	
		if number == int(response['results']['per_page'])-1:
				break
		

def company_number(args,api):
	api = api+f"companies/{args.jurisdiction}/{args.companynumber}"
	while True:
		if not args.jurisdiction:
			exit(f"{white}missing:  {green}-j{white}/{green}--jurisdiction-code{reset}")
		response = requests.get(api).json()
		pprint(response)
		if args.output:
			object = json.dumps(response, indent=4)
			with open(args.output, "a") as file:
				file.write(object)
				file.close()
		break
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
	start = datetime.now()
	while True:
		try:
			occli()
			if args.verbose:
				exit(f"\n{white}[{green}•{white}] Occli stopped in {red}{datetime.now()-start}{white} seconds.{reset}\n")
			break
			
		except IndexError:
		    if args.verbose:
		    	exit(f"{white}[{red}!{white}] Company: {args.companyname} {red}Not Found{white}.{reset}\n")
		    break
		  
		except KeyboardInterrupt:
		    if args.verbose:
		    	exit(f"\n{white}[{red}x{white}] Occli interrupted ({red}Ctrl{white}+{red}C{white}).{reset}\n")
		    break
		    
		except Exception as e:
		    if args.verbose:
		    	print(f"\n{white}[{red}!{white}] Error: {red}{e}{reset}")
		    	print(f"{white}[{green}*{white}] Retrying...{reset}")
