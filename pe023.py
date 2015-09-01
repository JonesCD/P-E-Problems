"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the
sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 200 Hertz
Dur = 250 # Set Duration To 250 ms == 1/4 second
############################
from math import sqrt
from sets import Set

num = 28123

def divisors(n):
	dlist = [1]
	for i in range(2, int(round(sqrt(n))) + 1):
		if n % i == 0:
			dlist.append(i)
			if i != (n / i):
				dlist.append(n / i)
	#dlist.append(n)
	return dlist

def summors(dlist):
	tot = 0
	for i in dlist:
		tot += i
	return tot

def isabundant(n):
	if n < summors(divisors(n)):
		return True
	else:
		return False

def listabundant(num):
	abundance = []
	val = 1
	while val < num + 1:
		if isabundant(val) == True:
			abundance.append(val)
		val += 1
	return Set(abundance)

def listcheck(num, flist):
	for i in flist:
		remains = num - i
		if remains < 0:
			return 0
		elif remains in flist:
				return 1
	return 0

def listnotsums(num):
	numlist = listabundant(num)
	numlist2 = []
	for n in range(1, num + 1):
		if not listcheck(n, numlist):
			numlist2.append(n)
			print len(numlist2)
	return numlist2

numlist2 = listnotsums(num)
print sum(numlist2)

############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)