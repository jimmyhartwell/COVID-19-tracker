import argparse

from params import ACTIVE, DEATHS, RECOVERED, CASE_NUMBERS
from tracker import get_flag, request_data


def short_summarize(country_infos, **kargs):
    summary = ""
    for country_info in country_infos:
        country_flag = get_flag(country_info)
        summary += f"{country_flag} "
        for k in kargs.keys():
            emoji = CASE_NUMBERS[k].emoji
            cases = country_info[k]
            summary += f" {emoji} {cases:,}"
        summary += " "
    print(summary[:-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("countries", help="Countries to get case numbers for. Omit to get numbers globally", nargs="*")
    parser.add_argument("-a", "--active", help="Show active cases", default=True, action="store_true")
    parser.add_argument("-d", "--deaths", help="Show deaths", default=False, action="store_true")
    parser.add_argument("-r", "--recovered", help="Show recovered cases", default=False, action="store_true")
    args = parser.parse_args()
    countries = []
    if args.countries:
        countries = args.countries

    data = request_data(",".join(countries), "country", 1)
    short_summarize(data, active=args.active, deaths=args.deaths, recovered=args.recovered)
