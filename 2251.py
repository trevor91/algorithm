import sys
from queue import Queue

def move(start,end,end_capacity):
	# a -> b
	empty = end_capacity - end
	if empty > start:
		return((0, start+end))
	else:
		return((start-empty, end+empty))


if __name__ == '__main__':
	cap = sys.stdin.readline().strip().split()
	cap = [int(x) for x in cap]
	over = set()
	q = Queue()
	q.put((0,0,cap[2]))

	over = set()
	while not q.empty():
		cnt = 0
		a,b,c = q.get()
		over.add((a,b,c))
		if a != 0:
			# a -> b
			temp = move(a,b,cap[1])
			temp = (temp[0],temp[1],c)
			if not temp in over:
				q.put(temp)
			
			# a -> c
			temp = move(a,c,cap[2])
			temp = (temp[0],b,temp[1])
			if not temp in over:
				q.put(temp)

			cnt += 1
		if b != 0:
			# b -> c
			temp = move(b,c,cap[2])
			temp = (a,temp[0],temp[1])
			if not temp in over:
				q.put(temp)
			
			# b -> a
			temp = move(b,a,cap[0])
			temp = (temp[1],temp[0],c)
			if not temp in over:
				q.put(temp)

			cnt += 1
		if c != 0:
			# c -> a
			temp = move(c,a,cap[0])
			temp = (temp[1],b,temp[0])
			if not temp in over:
				q.put(temp)

			# c -> b
			temp = move(c,b,cap[1])
			temp = (a,temp[1],temp[0])
			if not temp in over:
				q.put(temp)
	rst = [y for x,_,y in over if x==0]
	rst = sorted(rst)
	rst = [str(x) for x in rst]
	print(' '.join(rst))