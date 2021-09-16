import sys
import datetime
import unittest
from pathlib import Path


sys.path.append(str(Path().absolute().parent))


class TestBool(unittest.TestCase):
    def test_is_open(self):
        from jpxtime3 import is_open

        self.assertEqual(is_open(datetime.datetime(2019, 1, 1)), 0)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 8)), 0)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 9)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 10)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 15, 10)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 15, 13)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 15, 15)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 15, 30)), 0)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 16, 30)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 20, 0)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 4, 23, 59)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 0, 0)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 5, 20)), 1)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 5, 25)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 5, 27)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 5, 30)), 2)
        self.assertEqual(is_open(datetime.datetime(2019, 1, 5, 5, 40)), 0)
        # J-GATE3.0
        self.assertEqual(is_open(datetime.datetime(2021, 9, 17, 15, 9)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 17, 15, 10)), 2)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 17, 16, 30)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 17, 23, 59)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 18, 0, 0)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 18, 5, 20)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 18, 5, 25)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 18, 5, 30)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 8, 45)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 9, 0)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 15, 9)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 15, 10)), 2)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 15, 16)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 16, 30)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 21, 23, 59)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 0, 0)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 25)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 26)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 30)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 40)), 1)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 55)), 2)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 5, 55)), 2)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 6, 0)), 2)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 6, 1)), 0)
        self.assertEqual(is_open(datetime.datetime(2021, 9, 22, 9, 0)), 1)


class TestTradingDay(unittest.TestCase):
    def test_get_next_trading_day_adj(self):
        from jpxtime3 import get_next_trading_day_adj

        self.assertEqual(
            get_next_trading_day_adj(datetime.datetime(2019, 1, 4, 9)),
            datetime.date(2019, 1, 7),
        )
        self.assertEqual(
            get_next_trading_day_adj(datetime.datetime(2019, 1, 4, 0)),
            datetime.date(2019, 1, 7),
        )
        self.assertEqual(
            get_next_trading_day_adj(datetime.datetime(2019, 1, 7, 9)),
            datetime.date(2019, 1, 8),
        )

    def test_get_nominal_trading_day(self):
        from jpxtime3 import get_nominal_trading_day

        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 1, 4, 9)),
            datetime.date(2019, 1, 4),
        )
        self.assertIsNone(get_nominal_trading_day(datetime.datetime(2019, 1, 4, 16, 0)))
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 1, 4, 17, 0)),
            datetime.date(2019, 1, 7),
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 1, 7, 23, 0)),
            datetime.date(2019, 1, 8),
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 4, 26, 23, 59)),
            datetime.date(2019, 5, 7),
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 4, 27, 3, 0)),
            datetime.date(2019, 5, 7),
        )


class TestSessionTime(unittest.TestCase):
    def test_session_time(self):
        from jpxtime3 import SessionTime

        self.assertEqual(
            SessionTime(datetime.datetime(2019, 1, 4, 9)).opening_time_ds,
            datetime.datetime(2019, 1, 4, 9),
        )
        self.assertEqual(
            SessionTime(datetime.datetime(2019, 1, 4, 9)).closing_time_ds,
            datetime.datetime(2019, 1, 4, 15, 15),
        )
        self.assertEqual(
            SessionTime(datetime.datetime(2019, 1, 4, 9)).opening_time_ns,
            datetime.datetime(2018, 12, 28, 16, 30),
        )
        self.assertEqual(
            SessionTime(datetime.datetime(2019, 1, 4, 9)).closing_time_ns,
            datetime.datetime(2018, 12, 28, 5, 30),
        )


class TestDrift(unittest.TestCase):
    def test_get_next_trading(self):
        from jpxtime3 import get_next_opening, get_next_closing

        self.assertEqual(
            get_next_opening(datetime.datetime(2019, 1, 4, 9)),
            datetime.datetime(2019, 1, 4, 16, 30),
        )
        self.assertEqual(
            get_next_closing(datetime.datetime(2019, 1, 4, 10)),
            datetime.datetime(2019, 1, 7, 15, 15),
        )
        self.assertEqual(
            get_next_opening(datetime.datetime(2019, 1, 7, 10)),
            datetime.datetime(2019, 1, 7, 16, 30),
        )
        self.assertEqual(
            get_next_opening(datetime.datetime(2019, 1, 7, 23)),
            datetime.datetime(2019, 1, 8, 16, 30),
        )
        self.assertEqual(
            get_next_closing(datetime.datetime(2019, 1, 7, 23)),
            datetime.datetime(2019, 1, 9, 15, 15),
        )

    def test_get_prev_trading(self):
        from jpxtime3 import get_prev_opening, get_prev_closing

        self.assertEqual(
            get_prev_opening(datetime.datetime(2019, 1, 4, 9)),
            datetime.datetime(2018, 12, 27, 16, 30),
        )
        self.assertEqual(
            get_prev_closing(datetime.datetime(2019, 1, 4, 10)),
            datetime.datetime(2018, 12, 28, 15, 15),
        )
        self.assertEqual(
            get_prev_opening(datetime.datetime(2019, 1, 7, 10)),
            datetime.datetime(2018, 12, 28, 16, 30),
        )
        self.assertEqual(
            get_prev_opening(datetime.datetime(2019, 1, 7, 23)),
            datetime.datetime(2019, 1, 4, 16, 30),
        )
        self.assertEqual(
            get_prev_closing(datetime.datetime(2019, 1, 7, 23)),
            datetime.datetime(2019, 1, 7, 15, 15),
        )
