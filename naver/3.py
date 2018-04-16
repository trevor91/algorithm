import sys
read = lambda: sys.stdin.readline().strip()

def solution(N, S, T):
	# write your code in Python 3.6
	arr = [[0 for _ in range(N)] for _ in range(N)]
	sunk = 0
	not_sunk = 0

	for target in T.split():
		y,x = int(target[0:-1])-1, ord(target[-1])-65
		arr[y][x] = -1

	for position in S.split(','):
		hit = 0;
		start, end = position.split()
		start_y = int(start[0:-1])-1
		start_x = ord(start[-1])-65
		end_y = int(end[0:-1])
		end_x = ord(end[-1])-64
		if start_y > end_y: start_y, end_y = end_y, start_y
		if start_x > end_x: start_x, end_x = end_x, start_x
		for y in range(start_y, end_y):
			for x in range(start_x, end_x):
				if arr[y][x] == -1:
					hit += 1
		if((end_y - start_y) * (end_x - start_x) == hit):
			sunk += 1
		elif(hit>0):
			not_sunk += 1
	return("{0},{1}".format(sunk, not_sunk))

N = int(read())
S = read()
T = read()

# print(S)
print(solution(N,S,T))