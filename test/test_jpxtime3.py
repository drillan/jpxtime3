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
            datetime.date(2019, 1, 4)
        )
        self.assertIsNone(
            get_nominal_trading_day(datetime.datetime(2019, 1, 4, 16, 0))
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 1, 4, 17, 0)),
            datetime.date(2019, 1, 7)
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 1, 7, 23, 0)),
            datetime.date(2019, 1, 8)
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 4, 26, 23, 59)),
            datetime.date(2019, 5, 7)
        )
        self.assertEqual(
            get_nominal_trading_day(datetime.datetime(2019, 4, 27, 3, 0)),
            datetime.date(2019, 5, 7)
        )
    
    def test_get_next_trading(self):
        from jpxtime3 import get_next_trading
        
        self.assertEqual(
            get_next_trading(datetime.datetime(2019, 1, 4, 9), "open"),
            datetime.datetime(2019, 1, 7, 9)
        )
        self.assertEqual(
            get_next_trading(datetime.datetime(2019, 1, 4, 10), "close"),
            datetime.datetime(2019, 1, 7, 15, 15)
        )
        self.assertEqual(
            get_next_trading(datetime.datetime(2019, 1, 7, 10), "open"),
            datetime.datetime(2019, 1, 8, 9)
        )
        self.assertEqual(
            get_next_trading(datetime.datetime(2019, 1, 7, 23), "open"),
            datetime.datetime(2019, 1, 9, 9)
        )
        self.assertEqual(
            get_next_trading(datetime.datetime(2019, 1, 7, 23), "close"),
            datetime.datetime(2019, 1, 9, 15, 15)
        )
        self.assertIsNone(
            get_next_trading(datetime.datetime(2019, 1, 4, 8), "open")
        )
    
    def test_get_prev_trading(self):
        from jpxtime3 import get_prev_trading
        
        self.assertEqual(
            get_prev_trading(datetime.datetime(2019, 1, 4, 9), "open"),
            datetime.datetime(2018, 12, 28, 9)
        )
        self.assertEqual(
            get_prev_trading(datetime.datetime(2019, 1, 4, 10), "close"),
            datetime.datetime(2018, 12, 28, 15, 15)
        )
        self.assertEqual(
            get_prev_trading(datetime.datetime(2019, 1, 7, 10), "open"),
            datetime.datetime(2019, 1, 4, 9)
        )
        self.assertEqual(
            get_prev_trading(datetime.datetime(2019, 1, 7, 23), "open"),
            datetime.datetime(2019, 1, 7, 9)
        )
        self.assertEqual(
            get_prev_trading(datetime.datetime(2019, 1, 7, 23), "close"),
            datetime.datetime(2019, 1, 7, 15, 15)
        )
        self.assertIsNone(
            get_prev_trading(datetime.datetime(2019, 1, 4, 8), "open")
        )