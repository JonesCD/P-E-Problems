import math
import time

input = 20

i = 1
start = time.clock()
print "I am counting time"
while i < math.factorial(input):
	good = 0
	for j in range(2, input + 1):
		if i % j == 0:
			good += 1
		else:
			break
	if good == input - 1:
		print i
		break
	i += 1
	
end = time.clock()
print end - start