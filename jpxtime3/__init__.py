
# coding: utf-8

# In[ ]:

import os
import pickle
from datetime import time, date, datetime, timedelta
from dateutil.parser import parse


# In[ ]:

ONE_YEAR_TO_SECONDS_365 = 31536000
ONE_YEAR_TO_SECONDS_245 = 21168000
ONE_DAY_TO_SECONDS = 86400
holiday_jpx = 0
sq_days = 0
datadir = os.path.dirname(os.path.abspath(__file__))


# In[ ]:

class DaySession:

    def __init__(self, dt=datetime.now()):
        self.opening = time(9, 0)
        self.pre_closing = time(15, 10)
        self.closing = time(15, 15)


class NightSession:

    def __init__(self, dt=datetime.now()):
        self.opening = time(16, 30)
        if dt >= datetime(2016, 7, 19):
            self.pre_closing = time(5, 25)
            self.closing = time(5, 30)
        elif datetime(2011, 7, 19) <= dt < datetime(2016, 7, 19):
            self.pre_closing = time(2, 55)
            self.closing = time(3, 0)
        elif datetime(2010, 7, 21) <= dt < datetime(2011, 7, 19):
            self.pre_closing = time(23, 25)
            self.closing = time(23, 30)
        elif datetime(2008, 10, 14) <= dt < datetime(2010, 7, 21):
            self.pre_closing = time(19, 55)
            self.closing = time(20, 0)
        elif dt < datetime(2008, 10, 14):
            self.pre_closing = time(18, 55)
            self.closing = time(19, 0)


# In[ ]:

class Session:
    def __init__(self, dt=datetime.now()):
        init_holiday_jpx()
        self.dt = dt
        self.d = dt.date()
        self.wd = dt.weekday()
        self.ds = DaySession(dt)
        self.ns = NightSession(dt)
        self.t = dt.time()
        self.session_dict = {
            0: 'Regular_Session(NS)',
            1: 'Closing_Auction(NS)',
            2: 'Closed(NS2DS)',
            3: 'Regular_Session(DS)',
            4: 'Closing_Auction(DS)',
            5: 'Closed(DS2NS)',
            6: 'Regular_Session(NS)'
        }
        self.session = self.get_ses()
        self.session_name = self.session_dict[self.session]
        self.is_open = self._is_open()

    def get_ses(self):
        is_ses0 = lambda x: time(0, 0) <= x < self.ns.pre_closing
        is_ses1 = lambda x: self.ns.pre_closing <= x <= self.ns.closing
        is_ses2 = lambda x: self.ns.closing < x < self.ds.opening
        is_ses3 = lambda x: self.ds.opening <= x < self.ds.pre_closing
        is_ses4 = lambda x: self.ds.pre_closing <= x <= self.ds.closing
        is_ses5 = lambda x: self.ds.closing < x < self.ns.opening
        is_ses6 = lambda x: self.ns.opening <= x
        is_ses = (is_ses0, is_ses1, is_ses2, is_ses3, is_ses4, is_ses5,
                  is_ses6)
        for i, func in enumerate(is_ses):
            if func(self.t):
                return i

    def _is_open(self):
        if self.session in (2, 5):
            return 0
        func_dict = {
            0: self.is_open_ses0,
            1: self.is_open_ses1,
            3: self.is_open_ses3,
            4: self.is_open_ses4,
            6: self.is_open_ses6
        }
        return func_dict[self.session]()
    
    def is_holiday(self, d, wd):
        if wd in (5, 6) or d in holiday_jpx:
            return True
        else:
            return False

    def is_open_ses0(self):
        d = self.d - timedelta(days=1)
        wd = d.weekday()
        if self.is_holiday(d, wd):
            return 0
        else:
            return 1

    def is_open_ses1(self):
        d = self.d - timedelta(days=1)
        wd = d.weekday()
        if self.is_holiday(d, wd):
            return 0
        else:
            return 2

    def is_open_ses3(self):
        if self.is_holiday(self.d, self.wd):
            return 0
        else:
            return 1

    def is_open_ses4(self):
        if self.is_holiday(self.d, self.wd):
            return 0
        else:
            return 2

    def is_open_ses6(self):
        if self.is_holiday(self.d, self.wd):
            return 0
        else:
            return 1


# In[ ]:

class Sq:
    def __init__(self, year=365):
        init_sq_days()
        self.year = year
        if self.year == 245:
            init_holiday_jpx()

    def _to_tuple(self, data):
        data_type = type(data)

        def _tuple(data):
            return data

        def _list_set(data):
            return tuple(data)

        def _str(data):
            if len(data) == 4:
                data = '20' + data + '01'
            elif len(data) == 6:
                if data[:2] == '20':
                    data = data + '01'
                else:
                    data = '20' + data
            dt = parse(data)
            return dt.date().timetuple()[:2]

        def _int(data):
            return _str(str(data))

        def _datetime(data):
            return data.date().timetuple()[:2]

        def _date(data):
            return data.timetuple()[:2]

        func_dict = {
            tuple: _tuple,
            list: _list_set,
            set: _list_set,
            str: _str,
            int: _int,
            datetime: _datetime,
            date: _date
        }
        return func_dict[data_type](data)

    def get_sq(self, data):
        return sq_days[self._to_tuple(data)]

    def gen_is_holiday(self, t0, t1):
        if t0 > t1:
            raise ValueError
        while t0 <= t1:
            if t0.weekday() in (5, 6) or t0 in holiday_jpx:
                yield True
            else:
                yield False
            t0 = t0 + timedelta(days=1)

    def get_t(self, t0, t1):
        if type(t1) == date:
            t1_date = t1
            t1 = datetime.combine(t1, time(9, 0))
        else:
            t1_date = t1.date()
        t0_date = t0.date()
        t = t1 - t0
        if self.year == 245:
            holidays = sum((x for x in self.gen_is_holiday(t0_date, t1_date)))
            t = (t.total_seconds() - holidays * ONE_DAY_TO_SECONDS
                 ) / ONE_YEAR_TO_SECONDS_245
        else:
            t = t.total_seconds() / ONE_YEAR_TO_SECONDS_365
        return t


# In[ ]:

def init_holiday_jpx():
    global holiday_jpx
    if not holiday_jpx:
        file = os.path.join(datadir, 'holiday_jpx.pickle4')
        with open(file, 'rb') as f:
            holiday_jpx = pickle.load(f)


def init_sq_days():
    global sq_days
    if not sq_days:
        file = os.path.join(datadir, 'sq.pickle4')
        with open(file, 'rb') as f:
            sq_days = pickle.load(f)


def is_open(dt=datetime.now()):
    return Session(dt).is_open


def get_sq(data):
    return Sq().get_sq(data)


def get_t(t0, t1, year=365):
    return Sq(year=year).get_t(t0, t1)


