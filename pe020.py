"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################

def factorial(n):
	tot = 1
	for i in range(n, 0, -1):
		tot *= i
	return tot
	
def stringit(n):
	strnum = str(n)
	return strnum

def sumit(strnum):
	tot = 0
	for i in range(len(strnum)):
		tot += int(strnum[i])
	return tot

num = 100
print sumit(stringit(factorial(num)))

############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)