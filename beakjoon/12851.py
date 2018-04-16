import sys
from heapq import heappush, heappop
from array import array

if __name__ == '__main__':
	n, k = map(int,sys.stdin.readline().split())
	if n >= k:
		print(n-k)
		print(1)
	else:
		q = []
		heappush(q, (0,n))
		visited = array('l', [0] * 100001)
		visited[n] = 1
		shortest_time = 100001
		cnt_method = 0
		while q:
			cur_sec, n = heappop(q)
			if cur_sec > shortest_time:
				break
			if n == k:
				shortest_time = cur_sec
				cnt_method += 1
			else:
				if n < k and n < 100000 and (visited[n+1] == 0 or visited[n+1] >= cur_sec):
					heappush(q, (cur_sec+1, n+1))
					visited[n+1] = cur_sec
				if n > 0 and (visited[n-1] == 0 or visited[n-1] >= cur_sec):
					heappush(q, (cur_sec+1, n-1))
					visited[n-1] = cur_sec
				if n > 0 and n < k and n*2 < 100001 and (visited[n*2] == 0 or visited[n*2] >= cur_sec):
					heappush(q, (cur_sec+1, n*2))
					visited[n*2] = cur_sec
			visited[k] = 0
		print(shortest_time)
		print(cnt_method)