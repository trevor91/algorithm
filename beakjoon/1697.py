import sys
from queue import Queue
from array import array
read = lambda: sys.stdin.readline().strip().split()

if __name__ == '__main__':
	i = read()
	i = [int(x) for x in i]
	if i[0] == i[1]:
		print(0)
	elif i[0] > i[1]:
		print(i[0]-i[1])
	else:
		rst = 0
		done = False
		q1 = Queue()
		q2 = Queue()
		q1.put(i[0])
		overlap = array('b',[0]*100001)
		while not done:
			while not q1.empty():
				t = q1.get()
				q2.put(t)
				overlap[t] = 1
			rst+=1
			while not q2.empty():
				t2 = q2.get()
				if (t2-1) == i[1] or (t2+1) == i[1] or (t2*2) == i[1]:
					print(rst)
					done = True
					break
				if t2 > 0 and not overlap[t2-1]:
					q1.put(t2-1)
				if t2 < 100000 and t2 < i[1] and not overlap[t2+1]:
					q1.put(t2+1)
				if t2 < 50001 and not overlap[t2*2]:
					q1.put(t2*2)