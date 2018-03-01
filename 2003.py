import sys
from array import array
read = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	n,m = read().split()
	n,m = int(n), int(m)

	arr = read().split()
	arr = [int(x) for x in arr]
	arr = array('l', arr)

	cnt = 0
	s, l, r = 0,0,0 #sum, left, right
	while l < n and r < n:
		if s > m:
			s -= arr[l]
			l += 1
		elif s < m:
			s += arr[r]
			r += 1
		else:
			cnt+=1
			s -= arr[l]
			l += 1
	if s == m:
		cnt += 1
	print(cnt)
