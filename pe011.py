"""
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
import csv

filename = 'pe011-grid.txt'

grid = []

with open(filename, 'rb') as file:
	k = 0
	for row in file:
		nums = [int(n) for n in row.split()]
		grid.append(nums)
		k += 1

rows = k
columns = len(grid[0])
#print grid

nums = [0, 0, 0, 0]
maxnum = 0
maxseq = []

# going to multiply 4 numbers and check if product is biggest
def prod(vals):
	global maxnum, maxseq
	# maxnum = 0
	# maxseq = [0, 0, 0, 0]
	prodnum = 1
	for n in range(4):
		prodnum *= vals[n]
	#print prodnum,
	#print vals
	if prodnum > maxnum:
		maxnum = prodnum
		maxseq = vals
		return maxnum, maxseq
		

# check side to side
for r in range(rows):
	for c in range(columns - 3):
		nums = grid[r][c : c + 4]
		prod(nums)
	
print maxnum, 'side to side: ', maxseq
		
# check top to bottom
maxnum = 0
maxseq = []
nums = [0, 0, 0, 0]
for c in range(columns):
	for r in range(rows - 3):
		nums = [grid[r][c], grid[r + 1][c], grid[r + 2][c], grid[r + 3][c]]
		# for p in range(4):
			# nums[p] = grid[r + p][c]
		prod(nums)
	# print maxnum, maxseq
		
print maxnum, 'top to bottom: ', maxseq

# check diagonals top left to bottom right
maxnum = 0
maxseq = []
nums = [0, 0, 0, 0]
for r in range(rows - 3):
	for c in range(columns - 3):
		nums = [grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2], grid[r + 3][c + 3]]
		prod(nums)
		
print maxnum, 'top left diagonal: ', maxseq

# check diagonals bottom left to top right
maxnum = 0
maxseq = []
nums = [0, 0, 0, 0]
for r in range(3, rows):
	for c in range(columns - 3):
		nums = [grid[r][c], grid[r - 1][c + 1], grid[r - 2][c + 2], grid[r - 3][c + 3]]
		prod(nums)
		
print maxnum, 'bottom left diagonal: ', maxseq

############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)