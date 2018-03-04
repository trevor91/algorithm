import sys
from heapq import heappush, heappop
from queue import Queue
read = lambda: sys.stdin.readline()

def checkPosition(x,y):
	ret = []
	for i in range(4):
		pre_x = x + move_x[i]
		pre_y = y + move_y[i]
		if pre_x >= 0 and pre_y >= 0 and pre_x < c and pre_y < r:
			ret.append((pre_x,pre_y))
	return ret


if __name__ == '__main__':
	r, c = map(int, read().split())
	load = []
	d,s = (-1,0), (-1,0)
	stars = []
	for i in range(r):
		temp = read().strip()
		if d[0]	== -1: d = (temp.find('D'), i)
		if s[0]	== -1: s = (temp.find('S'), i)
		tmp =  temp.find('*') 
		if tmp != -1:
			stars.append((tmp,i))
		load.append([x for x in temp])
	move_x = [0,0,1,-1]
	move_y = [1,-1,0,0]
	before_cnt = -1
	visited = set()
	visited.add(s)
	seaQ = Queue()
	for star in  stars:
		seaQ.put(star)
	q = []
	heappush(q, (0, (s)))

	while q:
		cnt, (cur_x, cur_y) = heappop(q)
		load[cur_y][cur_x] = 'S'
		
		# find target
		if d in checkPosition(cur_x, cur_y):
			print(cnt+1)
			break

		# sea
		if before_cnt != cnt:
			change_sea = []
			while not seaQ.empty():
				cur_sea_x, cur_sea_y = seaQ.get()
				for x, y in checkPosition(cur_sea_x, cur_sea_y):
					if load[y][x] == '.':
						load[y][x] = '*'
						change_sea.append([x,y])
			for x, y in change_sea:
				seaQ.put((x,y))
				visited.add((x,y))
			before_cnt = cnt

		# go
		for x, y in checkPosition(cur_x, cur_y):
			if load[y][x] == '.' and not ((x,y) in visited):
				heappush(q,(cnt+1,(x,y)))
				visited.add((x,y))
		load[cur_y][cur_x] = '.'
	else:
		print("KAKTUS")