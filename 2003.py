import sys
from array import array
read = lambda: sys.stdin.readline()

if __name__ == '__main__':
	n,m = read().split()
	n,m = int(n), int(m)

	arr = read().split()
	arr = [int(x) for x in arr]
	arr = array('l', arr)

	cnt = 0
	s, l, r = arr[0],0,0 #sum, left, right
	while l!=n or r!=n:
		if s > m:
			s -= arr[l]
			l += 1
		elif s < m:
			r += 1
			if r == n:break
			s += arr[r]
		else:
			cnt += 1
			r += 1
			if r == n:break
			s += arr[r]
	print(cnt)
