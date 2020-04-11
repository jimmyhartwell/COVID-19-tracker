#!/Users/bach/workspace/default/default_env/bin/python3
from datetime import datetime
import requests
import flag
import argparse
from params import *
import termgraph as tg

WORLD_BASE_PATH = "https://corona.lmao.ninja/all"
COUNTRY_BASE_PATH = "https://corona.lmao.ninja/countries/{}"
HISTORICAL_BASE_PATH = "https://corona.lmao.ninja/v2/historical/{}?lastdays={}"
REQUEST_TYPES = {
    "world": WORLD_BASE_PATH,
    "country": COUNTRY_BASE_PATH,
    "historical": HISTORICAL_BASE_PATH,
}


def get_info(countries, world, last_days):
    if world:
        summary = request_data(WORLD_BASE_PATH, "world", last_days)
        summarize(summary[0], world)
        return
    countries = ",".join(countries)
    summary = request_data(countries, "country", last_days)
    historical_data = request_data(countries, "historical", last_days)
    for s, h in zip(summary, historical_data):
        summarize(s)
        summarize_history(h)


def request_data(countries, request_type, last_days):
    base_path = REQUEST_TYPES[request_type]
    request_link = base_path.format(countries, last_days)
    response = requests.get(request_link)
    if response.status_code != SUCCESS:
        raise NameError
    info = response.json()
    if type(info) is not list:
        info = [info]
    return info


def summarize(country_info, world=False):
    if not world:
        country_flag = get_flag(country_info)
        country = f"{country_flag}  {country_info[COUNTRY]}"
    else:
        country = "the world"

    updated = datetime.fromtimestamp(country_info[UPDATED_TIME] // 1000).strftime(
        "%d/%m/%Y %H:%M"
    )
    output = f"\n*** COVID-19 information in {country} on {updated} ***\n"
    output += f"-------------------------------------------------------\n"

    for k, v in CASE_NUMBERS.items():
        output += f"{v.emoji} {country_info[k]:,} {v.title}\n"
    print(output)

def get_flag(country_info):
    try:
        country_flag = flag.flag(country_info[COUNTRY_INFO][COUNTRY_ISO2])
    except:
        country_flag = ""
    return country_flag

def summarize_history(country_info):
    timeline = country_info[TIMELINE]
    cases = timeline[CASES]
    deaths = timeline[DEATHS]
    recovered = timeline[RECOVERED]
    actives = {k: cases[k] - deaths[k] - recovered[k] for k in cases.keys()}
    labels = list(cases.keys())
    data = [[actives[k], deaths[k], recovered[k]] for k in cases.keys()]
    draw_stacked_graph(labels, data)


def draw_stacked_graph(labels, data, graph_width=100):
    normal_dat = tg.normalize(data, graph_width)
    args = {"format": "{:<5.2f}", "suffix": "", "no_labels": False}
    colors = [
        tg.AVAILABLE_COLORS["blue"],
        tg.AVAILABLE_COLORS["red"],
        tg.AVAILABLE_COLORS["green"],
    ]
    tg.stacked_graph(labels, data, normal_dat, None, args, colors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", help="Number of days in the past to get case numbers for", type=int)
    parser.add_argument("countries", help="Countries to get case numbers for. Omit to get numbers globally", nargs="*")
    args = parser.parse_args()
    countries = []
    last_days = 15
    if args.countries:
        countries = args.countries
    if args.days:
        last_days = args.days
    get_info(countries, len(countries) == 0, args.days)
