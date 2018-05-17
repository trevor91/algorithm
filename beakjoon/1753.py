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
	s = array('b', [0]*(v+1))
	s_q = queue.Queue()

	for _ in range(e):
		temp_path = [int(x) for x in r()]
		if temp_path[1] != start:
			path[temp_path[0]].append([temp_path[1],temp_path[2]])
	s[start] = 1
	s_q.put(start)

	while not s_q.empty():
		sub_start = s_q.get()
		for target, w in path[sub_start]:
			flag = 0
			if s[target] == 0:
				s[target] = 1
				flag = 1
			if memo[sub_start] + w < memo[target]:
				memo[target] = memo[sub_start] + w
				flag = 1
			if flag:
				s_q.put(target)
	for i in range(1,len(memo)):
		if memo[i] == math.inf:
			print("INF")
		else:
			print(int(memo[i]))