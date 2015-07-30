"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import time
start = time.clock()
import winsound
Freq = 200 # Set Frequency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second
############################
grid = [20, 20]

def pathcounts(grid):
	if grid == [0, 0]:
		return 1
	paths = 0
	
	if grid[0] > 0:
		paths += pathcounts([grid[0] - 1, grid[1]])
		
	if grid[1] > 0:
		paths += pathcounts([grid[0], grid[1] - 1])
		
	return paths

print pathcounts(grid)
############################
end = time.clock()
print 'elapsed time:',end - start
winsound.Beep(Freq,Dur)