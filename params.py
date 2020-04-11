from collections import namedtuple

# Country info
COUNTRY = "country"
COUNTRY_INFO = "countryInfo"
COUNTRY_ISO2 = "iso2"

# Cases info
UPDATED_TIME = "updated"
CASES = "cases"
TODAY_CASES = "todayCases"
DEATHS = "deaths"
TODAY_DEATHS = "todayDeaths"
RECOVERED = "recovered"
ACTIVE = "active"
CRITICAL = "critical"
CASES_PER_MILLION = "casesPerOneMillion"
DEATHS_PER_MILLION = "deathsPerOneMillion"
TESTS = "tests"
TESTS_PER_MILLION = "testsPerOneMillion"

# Historical info
TIMELINE = "timeline"

# Friendly info
Info = namedtuple("Info", ["title", "emoji"])

CASE_NUMBERS = {
    CASES: Info("total cases", "😷"),
    TODAY_CASES: Info("new cases", "🤒"),
    DEATHS: Info("deaths", "💀"),
    TODAY_DEATHS: Info("new deaths", "😥"),
    RECOVERED: Info("recovered", "💪"),
    ACTIVE: Info("active cases", "🤒"),
    TESTS: Info("tests", "🧪"),
}

# Header code
SUCCESS = 200

# Error messages
ERROR = "Cannot load information at the moment"
