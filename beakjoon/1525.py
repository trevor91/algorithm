# 0인 자리를 찾아서.
# x,y 위치에서 0~2 범위에서 하나만 +1 or -1하는 위치로 이동 가능.
# 이전에 한 상태로 가는건 x (중복체크 해야함)
# 

import sys
from queue import Queue
from array import array
read = lambda: sys.stdin.readline().strip().split()

if __name__ == '__main__':
	ans = "123456780"
	mat = [read() for _ in range(3)]
	mat = [xx for x in mat for xx in x]
	mat = ''.join(mat)
	q = Queue()
	q.put(mat)
	overlap = {mat:0}

	while True:
		mat = q.get()
		# print(mat)
		if ans == mat:
			print(overlap[mat])
			break
		zero = mat.find('0')
		if zero == 0: change_idx = [1,3]
		elif zero == 1: change_idx = [0,2,4]
		elif zero == 2: change_idx = [1,5]
		elif zero == 3: change_idx = [0,4,6]
		elif zero == 4: change_idx = [1,3,5,7]
		elif zero == 5: change_idx = [2,4,8]
		elif zero == 6: change_idx = [3,7]
		elif zero == 7: change_idx = [4,6,8]
		elif zero == 8: change_idx = [5,7]
		
		for i in change_idx:
			if zero < i: i1, i2 = zero, i
			else: i1, i2 = i, zero
			temp = mat[:i1]+mat[i2]+mat[i1+1:i2]+mat[i1]+mat[i2+1:]
			if overlap.get(temp) != None:
				continue
			q.put(temp)
			overlap[temp] = overlap[mat] + 1
		
		if q.empty():
			print(-1)
			break