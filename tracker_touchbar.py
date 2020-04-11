import argparse

from params import CASE_NUMBERS, ACTIVE
from tracker import get_flag, request_data


def short_summarize(country_infos):
    summary = CASE_NUMBERS[ACTIVE].emoji
    for country_info in country_infos:
        country_flag = get_flag(country_info)
        active = country_info[ACTIVE]
        summary += f" {country_flag} {active:,}"
    print(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("countries", help="Countries to get case numbers for. Omit to get numbers globally", nargs="*")
    args = parser.parse_args()
    countries = []
    if args.countries:
        countries = args.countries
    data = request_data(",".join(countries), "country", 1)
    short_summarize(data)
