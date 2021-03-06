"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def convert(n):
	nstr = str(n)
	length = len(nstr)
	
	if length == 1:
		print ones[n]
		return len(ones[n])
		
	elif length == 2:
		if nstr[0] == '1':
			print teens[int(nstr[1])]
			return len(teens[int(nstr[1])])
		elif nstr[1] == '0':
			print tens[int(nstr[0])]
			return len(tens[int(nstr[0])]) 
		else:
			print tens[int(nstr[0])] + ' ' + ones[int(nstr[1])]
			return len(tens[int(nstr[0])] + ones[int(nstr[1])])
			
			
	elif length == 3:
		if nstr[1] == '0' and nstr[2] == '0':
			print ones[int(nstr[0])] + ' hundred'
			return len(ones[int(nstr[0])] + 'hundred')
			
		else:
			if nstr[1] == '0':
				print ones[int(nstr[0])] + ' hundred and ' + ones[int(nstr[2])]
				return len(ones[int(nstr[0])] + 'hundredand' + ones[int(nstr[2])])
			elif nstr[1] == '1':
				print ones[int(nstr[0])] + ' hundred and ' + teens[int(nstr[2])]
				return len(ones[int(nstr[0])] + 'hundredand' + teens[int(nstr[2])])
			elif nstr[2] == '0':
				print ones[int(nstr[0])] + ' hundred and ' + tens[int(nstr[1])]
				return len(ones[int(nstr[0])] + 'hundredand' + tens[int(nstr[1])])
			else:
				print ones[int(nstr[0])] + ' hundred and ' + tens[int(nstr[1])] + ' ' + ones[int(nstr[2])]
				return len(ones[int(nstr[0])] + 'hundredand' + tens[int(nstr[1])] + ones[int(nstr[2])])
				
	else:
		print 'one thousand'
		return len('onethousand')
	
def tests(n):
	print letterones(n)
	
def summation(n):
	tot = 0
	for num in range(1, n + 1):
		tot += convert(num)
	return tot
		
print summation(1000)
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)