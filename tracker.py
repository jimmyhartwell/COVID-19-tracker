#!/Users/bach/workspace/default/default_env/bin/python3

import os
import requests
import json
from params import *
import flag
from datetime import datetime
import argparse

COUNTRY_BASE_LINK = f"https://corona.lmao.ninja/countries/"

def get_infos(countries):
    countries = ','.join(countries)
    request_link = os.path.join(COUNTRY_BASE_LINK, countries)
    response = requests.get(request_link)
    if response.status_code != SUCCESS:
        raise NameError

    infos = response.json()
    if type(infos) is not list:
        infos = [infos]
    return infos

def output_info(info):
    country = flag.flag(info[COUNTRY_INFO][COUNTRY_ISO2])
    updated = datetime.fromtimestamp(info[UPDATED_TIME]//1000).strftime("%d/%m/%Y %H:%M")
    output = f"*** COVID-19 information in {country}  on {updated} ***\n"
    output += f"-------------------------------------------------------\n"
    
    for k, v in CASE_NUMBERS.items():
        output += f"{v.emoji} {info[k]} {v.title}\n"
    print(output)

def main(countries):
    try:
        infos = get_infos(countries)
        [output_info(info) for info in infos]
    except NameError:
        print(ERROR)

parser = argparse.ArgumentParser(description="COVID-19 Information Around the World")
parser.add_argument("countries", nargs="+", help="Country to get information for")
parser.add_argument("-n", dest="main", action="store_const", const=main)
args = parser.parse_args()
args.main(args.countries)