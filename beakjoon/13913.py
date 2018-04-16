import sys
from queue import Queue
from array import array
read = lambda: sys.stdin.readline().strip().split()

if __name__ == '__main__':
	i = read()
	i = [int(x) for x in i]
	if i[0] == i[1]:
		print('0\n%d\n'%i[0])
	elif i[0] > i[1]:
		print(i[0]-i[1])
		temp = i[0]
		while i[1] != temp:
			print(temp, end = ' ')
			temp-=1
		print(temp)
	else:
		overlap = array('b',[0]*150001)
		path = array('l',[0]*150001)
		q = Queue()
		q.put(i[0])
		overlap[i[0]] = 1
		while not q.empty():
			t = q.get()
			if (t-1) == i[1] or (t+1) == i[1] or (t*2) == i[1]:
				path[i[1]] = t
				break
			if t > 0 and not overlap[t-1]:
				q.put(t-1)
				path[t-1] = t
				overlap[t-1] = 1
			if t < 100000 and t < i[1] and not overlap[t+1]:
				q.put(t+1)
				path[t+1] = t
				overlap[t+1] = 1
			if t < 75000 and not overlap[t*2]:
				q.put(t*2)
				path[t*2] = t
				overlap[t*2] = 1
		idx = i[1]
		temp = [str(idx)]
		while True:
			temp.append(str(path[idx]))
			idx = path[idx]
			if idx == i[0]:
				break
		print(len(temp)-1)
		print(' '.join(temp[::-1]))
