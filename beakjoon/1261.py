import sys
from array import array
from queue import Queue
from heapq import heappush, heappop
read = lambda: sys.stdin.readline()
conv = lambda x, y: m*x+y

if __name__ == '__main__':
	m,n = map(int, read().split())
	mat = array('b',[])
	for i in range(n):
		mat.extend(map(int, read().strip()))

	p_x=[0,0,1,-1]
	p_y=[-1,1,0,0]
	visited = array('b',[0]*(m*n))
	cnt = array('l',[0]*(m*n))
	q = []
	heappush(q, (0,(0,0)))

	while q:
		cur_x, cur_y = heappop(q)[1]
		cur_idx = conv(cur_x,cur_y)
		if cur_idx == len(mat)-1:
			print(cnt[cur_idx])
			break

		for x, y in zip(p_x, p_y):
			pre_x, pre_y = cur_x + x, cur_y + y
			if pre_x > -1 and pre_y > -1 and pre_x < n and pre_y < m:
				pre_idx = conv(pre_x,pre_y)
				if visited[pre_idx] == 0:
					visited[pre_idx] = 1
					cnt[pre_idx] = cnt[cur_idx] + mat[pre_idx]
					heappush(q, (cnt[pre_idx],(pre_x,pre_y)))