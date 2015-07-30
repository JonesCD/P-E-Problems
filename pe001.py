tot = 0
for i in range(1, 1000):
    if i % 3 == 0:
        tot = tot + i
        print i
        i += 1
    elif i % 5 == 0:
        tot = tot + i
        print i
        i += 1
    else:
        i += 1
print "total:"
print tot