"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
def summation(base, exp):
	n = base**exp
	nstr = str(n)
	tot = 0
	for digit in nstr:
		tot += int(digit)
	return tot

print summation(2, 1000)
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)