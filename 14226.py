import sys
from queue import Queue
if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	
	q = Queue()
	q.put([1,0,0]) #[cnt, clip, sec]
	over = set()
	while not q.empty():
		i = q.get()
		if i[0] == n:
			print(i[2])
			break
		
		if (i[0], i[1]) in over:
			continue
		
		over.add((i[0],i[1]))
		
		#paste
		if i[1] != 0:
			temp = [i[0]+i[1], i[1], i[2]+1]
			q.put(temp)

		#store
		if i[0] != i[1]:
			temp = [i[0], i[0], i[2]+1]
			q.put(temp)

		#delete
		if i[0] > 2:
			temp = [i[0]-1, i[1], i[2]+1]
			q.put(temp)
