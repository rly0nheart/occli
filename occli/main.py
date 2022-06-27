#!/usr/bin/env python3

import logging
import argparse
import requests
from datetime import datetime
from occli.banner import versionTag, nameLogo

global args
global start_time
# Parsing command line arguments
parser = argparse.ArgumentParser(description="Occli — by Richard Mwewa | https://about.me/rly0nheart",epilog="A command line tool that queries the Open Corporates Database and returns data on corporations under the copyleft Open Database License.")
parser.add_argument("query", metavar="query")
parser.add_argument("-c","--count", help="number of results to return (1-30) (default: %(default)s)", default=30, type=int)
parser.add_argument("-o","--output", help=argparse.SUPPRESS)
parser.add_argument("-v","--verbose",help="enable verbosity",action="store_true")
args = parser.parse_args()
start_time = datetime.now()
if args.verbose:
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S%p', level=logging.DEBUG)

print(nameLogo)
# searching compan(y)(ies) on OpenCorporates    	
def onSearch():
    try:
        interval = 0
        response = requests.get(f"https://api.opencorporates.com/v0.4.8/companies/search?q={args.query}*").json()
        if response['results']['companies'] == []:
            logging.info(f"No results found for query ({args.query}). Try a different search or try again later.")
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
                
                if number == args.count-1:
                    break
                elif number == int(response['results']['per_page'])-1:
                    break
                else:
                    pass
                    
        logging.info(f"Returned {args.count} results for query ({args.query}) in {datetime.now()-start_time} seconds.")
                    
    except KeyboardInterrupt:
        logging.info("Process interrupted with (Ctrl+C).")
        
    except IndexError:
        pass
        
    except Exception as e:
        logging.error(f"An error occured: {e}")
