import time
input = 100

totsumonly = 0
totsqsum = 0
start = time.clock()
print "I am counting time"
i = 0
j = 0
while i < input + 1:
	j = i ** 2
	totsumonly += j
	i += 1
print totsumonly

tempsum = 0
k = 0
while k < input + 1:
	tempsum += k
	k += 1
	
totsqsum = tempsum ** 2
print totsqsum

print "diff of sum of squares: "
print totsqsum - totsumonly
end = time.clock()
print end - start