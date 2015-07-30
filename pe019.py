"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
def days(month, year):
	if month == 3 or month == 5 or month == 8 or month == 10:
		return 30
	elif month == 1:
		return feb(year)
	else:
		return 31

def feb(year):
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 != 0:
			return 28
		else:
			return 29
	else:
		return 28

day = 1
year = 1900
monthrange = range(12)
totdays = 0

for year in range(1900, 2001):
	for month in monthrange:
		if day == 0:
			print 'match: month %r, year %r' %(month, year)
			totdays += 1
		day = (day + days(month, year)) % 7
print totdays - 2      # two happen in 1900 so take those out

	
	
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)