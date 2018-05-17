import sys
from array import array
import queue
import math
r = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
	v,e = map(int,r())
	start = int(r()[0])
	path = [[] for _ in range(v+1)]
	memo = array('f',[math.inf]*(v+1))
	memo[start] = 0
	s = set()
	s_q = queue.Queue()
	q = list(range(1,v+1))

	for _ in range(e):
		temp_path = [int(x) for x in r()]
		if temp_path[1] != start:
			path[temp_path[0]].append([temp_path[1],temp_path[2]])
	s.add(start)
	s_q.put(start)
	q.remove(start)
	while not s_q.empty():
		sub_start = s_q.get()
		for target, weght in path[sub_start]:
			if not target in s:
				s_q.put(target)
				q.remove(target)
				s.add(target)
			if memo[sub_start] + weght < memo[target]:
				memo[target] = memo[sub_start] + weght
				s_q.put(target)

	for i in range(1,len(memo)):
		if memo[i] == math.inf:
			print("INF")
		else:
			print(int(memo[i]))