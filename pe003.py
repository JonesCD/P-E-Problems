import math

start = 600851475143  

i = 1

while i <= math.sqrt(start):
	if start % i == 0:
		numb = 0
		j = 2
		while j <= math.sqrt(i):
			if i % j == 0:
				numb += 1
				j += 1
			else:
				j += 1
		if numb == 0:
			print i
		
	i += 1