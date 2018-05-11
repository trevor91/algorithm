import sys
from heapq import heappop, heappush
r = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
	m,n = map(int, r())
	arr = []
	heap = []
	for _ in range(n):
		arr.append([int(x) for x in r()])
	
	#find 1 position
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if(arr[y][x] == 1):
				heappush(heap, (0,(y,x)))

	move_x = [0,0,-1,1]
	move_y = [1,-1,0,0]
	day = -1
	while heap:
		day, (y,x) = heappop(heap)

		for temp_y, temp_x in zip(move_y, move_x):
			temp_y += y
			temp_x += x
			if temp_y >= n or temp_x >= m or temp_y < 0 or temp_x < 0:
				continue
			if arr[temp_y][temp_x] == 0:
				arr[temp_y][temp_x] = 1
				heappush(heap, (day+1,(temp_y, temp_x)))
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if(arr[y][x] == 0):
				day = -1
				break
		if day == -1:
			break
	print(day)
