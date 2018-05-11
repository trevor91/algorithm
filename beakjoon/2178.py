import sys
from heapq import heappush, heappop
r = lambda: sys.stdin.readline()

if __name__ == '__main__':
	n,m = map(int,r().split())
	y = 0
	x = 0
	move_x = [0,0,1,-1]
	move_y = [1,-1,0,0]
	arr = []
	visited = set()
	heap = []
	heappush(heap, (1,(y,x)))
	for _ in range(n):
		arr.append([int(x) for x in r().strip()])
	
	while heap:
		cnt, (y,x) = heappop(heap)
		for my, mx in zip(move_y, move_x):
			if y+my >= n or x+mx >= m or y+my < 0 or x+mx < 0:
				continue
			if arr[y+my][x+mx] == 0:
				continue
			if (y+my, x+mx) in visited:
				continue
			if y+my+1==n and x+mx+1==m:
				print(cnt+1)
				heap = []
				break
			visited.add((y+my,x+mx))
			heappush(heap, (cnt+ 1, (y+my,x+mx)))