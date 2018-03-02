import sys
from array import array
read = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
	n,m = read()
	n,m = int(n), int(m)

	arr = read()
	arr = [int(x) for x in arr]
	arr = array('l', arr)

	length = 100000
	s, l, r = arr[0],0,1 #sum, left, right
	while not (l == n and r == n):
		if arr[l] >= m:
			length = 1
			break
		if s >= m:
			if length > r-l:
				length = r-l
			s -= arr[l]
			l += 1
		elif s < m:
			if r==n:
				break
			s += arr[r]
			r += 1
		
	if length== 100000:
		print(0)
	else:
		print(length)
