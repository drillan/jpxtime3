import datetime
import pickle
from urllib import request

import yaml

holidays_yml = (
    "https://raw.githubusercontent.com/holiday-jp/holiday_jp/master/holidays.yml"
)


def get_holidays(url):
    yml_data = request.urlopen(url)
    return set(yaml.load(yml_data, yaml.FullLoader).keys())


def set_jpxholidays(data, start, end):
    for i in range(start, end + 1):
        data.add(datetime.date(i, 1, 2))
        data.add(datetime.date(i, 1, 3))
        data.add(datetime.date(i, 12, 31))
    return tuple(sorted(data))


def save_data(data, path, protocol=4):
    with open(path, "wb") as f:
        pickle.dump(data, f, protocol=protocol)


def main():
    holidays = get_holidays(holidays_yml)
    jpx_holidays = set_jpxholidays(holidays, 1970, 2050)
    save_data(jpx_holidays, "jpxtime3/holiday_jpx.pickle4")


if __name__ == "__main__":
    main()
