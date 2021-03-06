"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
from math import sqrt, ceil

def factors(n):
	factorlist = [1]
	for i in range(2, int(ceil(sqrt(n)))):
		if n % i == 0:
			factorlist.append(i)
			factorlist.append(n / i)
	# factorlist.pop(n)
	return factorlist

def amicable(n):
	global tot
	m = sum(factors(n))
	if sum(factors(m)) == n and n != m:
		print 'AMICABLE!'
		print n, m
		return n
	else:
		return 0

tot = 0
for i in range(10000):
	tot += amicable(i)
print tot
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)