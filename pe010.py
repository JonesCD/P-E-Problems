"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################

from math import sqrt
from math import ceil

maxnum = 2000000
n = 2
numlist = [2]

for n in range(3, maxnum, 2):
	isprime = 1
	for j in range(3, int(ceil(sqrt(n))) + 1, 2):
		if n % j == 0:
			isprime = 0
			break
	
	if isprime == 1:
		numlist.append(n)
		
# print numlist
print sum(numlist)
print len(numlist)

############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)