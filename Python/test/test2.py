for x in range(10000):
	if x % 2 == 1 and x % 3 == 0 and x % 4 == 1 and \
    x % 5 == 4 and x % 6 == 3 and x % 7 == 0 and x % 8 == 1 and x % 9 == 0:
		print(x)
		break
for x in range(10000):
	if x % 5 == 4 and x % 6 == 3 and x % 7 == 0 and x % 8 == 1 and x % 9 == 0:
		print(str(x) + '--')
for x in range(9):
	print(str(x + 1) + '---' + str(609 % (x + 1)))
