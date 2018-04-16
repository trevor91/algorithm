import sys
from queue import Queue
from array import array

if __name__ == '__main__':
	n, k = sys.stdin.readline().split()
	n, k = int(n), int(k)

	sec = array('l',[0]*100001)
	visited= array('l',[0]*100001)
	q = Queue()
	q.put(n)
	while True:
		n = q.get()
		if n == k:
			print(sec[n])
			break
		else:
			i = 2
			while True:
				if n*i < k and visited[n*i] == 0:
					q.put(n*i)
					sec[n*i] = sec[n]
					visited[n*i] = 1
					i *= 2
				else:
					break
			if n*i < 100002 and visited[n*i] == 0:
				q.put(n*i)
				sec[n*i] = sec[n]
				visited[n*i] = 1
				if n*i*2 < 100002:
					visited[n*i*2] = 1

			if n > 0 and visited[n-1] == 0:
				q.put(n-1)
				sec[n-1] = sec[n] + 1
				visited[n-1] = 1
			if n < k and visited[n+1] == 0:
				q.put(n+1)
				sec[n+1] = sec[n] + 1
				visited[n+1] = 1
			