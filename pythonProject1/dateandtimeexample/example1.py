import datetime as gm
from datetime import datetime as syd
import datetime as syt
from datetime import date
from datetime import time
from datetime import datetime, timedelta

print(dir(gm))
today = gm.date.today()

print('Today\'s Date = ', today)
print('Year     = ', today.year)
print('Month = ', today.month)
print('Day     = ', today.day)
print('Maximum Year  = ', gm.MAXYEAR)
print('Minimum Year  = ', gm.MINYEAR)

dt = gm.datetime.now()
print(dt)

print('Today\'s Dt = ', dt)

print()
dt = gm.date.today()

print('\nToday\'s Dt = ', dt)

dt = syd.now()

print('Date           = ', dt)
print('Short Date = ', dt.date())
print('Year           = ', dt.year)
print('Month          = ', dt.month)
print('Day            = ', dt.day)
print('Time           = ', dt.time())
print('Hour           = ', dt.hour)
print('Minute         = ', dt.minute)
print('Second         = ', dt.second)
print('Microsecond    = ', dt.microsecond)
print('Weekday Number = ', dt.weekday())

time = syd.time(syd.now())

print('Current Time                  = ', time)
print('Hour from Current Time        = ', time.hour)
print('Minute from Current Time      = ', time.minute)
print('Second from Current Time      = ', time.second)
print('Microsecond from Current Time = ', time.microsecond)

print(syd.now())
print(syd.now().isoformat())

dt1 = syd(2017, 12, 31)
print(dt1)

dt4 = syd(2014, 12, 31, 22, 33, 44)
print(dt4)

dt5 = syd(2016, 12, 31, 22, 33, 44, 123456)
print(dt5)

dt = syd.now()
print(dt)

dt_replace = dt.replace(hour=2)
print(dt_replace)

dt_replace2 = dt.replace(minute=59)
print(dt_replace2)

dt_replace3 = dt.replace(second=4)
print(dt_replace)

dt_replace4 = dt.replace(microsecond=7)
print(dt_replace4)

dt = syt.date(2018, 12, 31)

tm = syt.time(23, 59, 58)

tm2 = syt.time(23, 0)

combine_dt = syt.datetime.combine(dt, tm)
combine_dt2 = syt.datetime.combine(dt, tm2)

print('Date           = ', dt)
print('Time           = ', tm)
print('Time2          = ', tm2)
print('Date and Time  = ', combine_dt)
print('Date and Time2 = ', combine_dt2)

print('Year           = ', combine_dt.year)
print('Month          = ', combine_dt.month)
print('Day            = ', combine_dt.day)
print('Hour           = ', combine_dt.hour)
print('Minute         = ', combine_dt.minute)
print('Second         = ', combine_dt.second)
print('Microsecond    = ', combine_dt.microsecond)

dt = date(2018, 1, 31)
print(dt)
print(dt.isoformat())

dt = date.today()

print('Today\'s Date  = ', dt)
print('Year           = ', dt.year)
print('Month          = ', dt.month)
print('Day            = ', dt.day)
print('Weekday Number = ', dt.weekday())
print('\nMinimum          = ', date.min)
print('Maximum         = ', date.max)
print('Resolution       = ', date.resolution)

dt = datetime.now()

print('Dt         = ', dt)

future_dt = dt + timedelta(days=365)
print('Future = ', future_dt)

past_dt = dt - timedelta(days=730)
print('Past    = ', past_dt)

print("\n-----strftime Results----")
dt2 = dt.strftime('%Y-%m-%d')
print(dt2)

dt3 = dt.strftime('%Y/%m/%d %H:%M:%S %p')
print(dt3)

dt4 = dt.strftime('%B %d, %Y %I-%M-%S %p')
print(dt4)

print("\n-----strptime Results----")
dt_str = '31 December 2017'
dt_value = dt.strptime(dt_str, '%d %B %Y')
print(dt_value)

dt_str2 = '15/8/17 22:33:55'
dt_value2 = dt.strptime(dt_str2, '%d/%m/%y %H:%M:%S')
print(dt_value2)