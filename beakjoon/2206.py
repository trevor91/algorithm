import sys
from heapq import heappop, heappush
from array import array
read = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
	max_y, max_x = map(int,read())
	arr = [read()[0] for _ in range(max_y)]

	move_x = [0,0,1,-1]
	move_y = [1,-1,0,0]
	visited = set((0,0,0))
	q = []
	data = (1, (0,0,0)) #(지나온 회수, (x,y,벽을 깬 여부))
	heappush(q,data)
	
	while q:
		cnt, (cur_x, cur_y, wall) =  heappop(q)
		if cur_y == (max_y-1) and  (cur_x == max_x-1):
			print(cnt)
			break

		for i in range(4):
			pre_x = cur_x + move_x[i]
			pre_y = cur_y + move_y[i]
			if pre_x >= 0 and pre_y >= 0 and pre_x < max_x and pre_y < max_y:
				temp = (pre_x, pre_y, wall + int(arr[pre_y][pre_x]))
				if temp[2] == 2 and wall == 1:
					continue
				elif not (temp in visited):
					heappush(q, (cnt+1, temp))
					visited.add(temp)
	else:
		print(-1)