collatz = {}
def lengthChain(startingNum):

	originalNum = startingNum
	length = 1
	

	while startingNum != 1:

		if startingNum in collatz:
			collatz[originalNum] = collatz[startingNum] + length
			return originalNum, collatz[originalNum]

		if startingNum % 2 == 0 :
			startingNum = startingNum / 2
		else:
			startingNum = 3 * startingNum + 1
		length +=1

	collatz[originalNum] = length

	return (originalNum, length)

def longestChain(cap):
	longestChainNum = (2,2)

	for i in range( 2 , cap):
		attempt = lengthChain(i)
		if attempt[1] > longestChainNum[1]:
			longestChainNum = attempt

	return longestChainNum


print longestChain(1000000)