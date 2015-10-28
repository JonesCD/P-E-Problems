"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################

def adding(i):
	numsum = 0
	for n in range(1, i, 2):
		numsum += n
	return numsum

def divisors(i):
	superlist = [1]
	for n in range(2, (i / 2 + 1)):
		if i % n == 0:
			superlist.append(n)
	superlist.append(i)
	return superlist
	
# def listsize(i):
	# if len(i) > 500:
		# return False
		# print "BAM!"

k = 1
superlist = []		
while len(superlist) < 5:
	num = adding(k)
	superlist = divisors(num)
	print k, num, len(superlist)
	k += 1
	
print superlist
	
	
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)