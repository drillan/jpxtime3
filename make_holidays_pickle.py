import datetime
import pickle

import yaml


def get_holidays(file):
    with open (file) as yml_data:
        return set(yaml.load(yml_data, yaml.FullLoader).keys())


def set_jpxholidays(data, start, end):
    for i in range(start, end + 1):
        data.add(datetime.date(i, 1, 2))
        if i < 2022:
            data.add(datetime.date(i, 1, 3))
        data.add(datetime.date(i, 12, 31))
    return tuple(sorted(data))


def save_data(data, path, protocol=4):
    with open(path, "wb") as f:
        pickle.dump(data, f, protocol=protocol)


def main():
    # "https://raw.githubusercontent.com/holiday-jp/holiday_jp/master/holidays.yml"
    holidays_yml = "holidays.yml"
    holidays = get_holidays(holidays_yml)
    jpx_holidays = set_jpxholidays(holidays, 1970, 2023)
    save_data(jpx_holidays, "jpxtime3/holiday_jpx.pickle4")


if __name__ == "__main__":
    main()
