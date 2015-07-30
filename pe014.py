"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
def evens(n):
	n = n / 2
	return n

def odds(n):
	n = 3 * n + 1
	return n

def collatz(n):
	#sequence = [n]
	starter = n
	length = 1
	while n != 1:
		if n % 2 == 0:
			n = evens(n)
			length += 1
			#sequence.append(n)
		
		else:
			n = odds(n)
			length += 1
			#sequence.append(n)
	#return len(sequence), sequence[0]
	return length, starter
		
def countitup(n):
	#countz = []
	maxcountz = 0
	for num in range(1, n):
		k = collatz(num)
		if k[0] > maxcountz:
			maxcountz = k
		#countz.append(k)
	return maxcountz
			
print countitup(1000000)

	
	
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)