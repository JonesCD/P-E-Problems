"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
filename = 'p022_names.txt'

with open(filename, 'rb') as file:
	for row in file:
		names = row

namessorted = names.split('","')

numnames = len(namessorted)

print namessorted
print numnames



############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)