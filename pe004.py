a = 999
b = 999

pallist = []
for one in range(a, 1, -1):
	for two in range(b, 1, -1):
		pal = one * two 
		palstr = str(pal)
		revpalstr = palstr[::-1]
		if palstr == revpalstr:
			print pal
			pallist.append(pal)
			break
			
print max(pallist)