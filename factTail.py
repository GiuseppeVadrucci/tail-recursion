def factTail(n,acc):
	return acc if n == 1 else factTail(n-1,acc*n)


if __name__ == '__main__':
	for i in [5,7,15,25,30]:
		print('fact({0:3d}) :- {1}'.format(i,factTail(i,1)))
