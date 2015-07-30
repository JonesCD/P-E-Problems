"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""
import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################

import math

# a = 0
# b = 0 
# c = 0
goal = 1000

for a in range(goal / 2):
	for b in range(goal / 2):
		c = math.sqrt(a**2 + b **2)
		if c % 1 == 0:
			if a + b + c == goal and c > b and a < b:
				print a, b, int(c)
				print int(a * b * c)		
				
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)