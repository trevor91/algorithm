import sys
read = lambda: sys.stdin.readline()
sys.setrecursionlimit(100000)

def binary(start, end):
	mid = (start+end) // 2
	if end - start < 2:
		rst1 = sum(map(lambda x:x//mid, cables))
		rst2 = sum(map(lambda x:x//(mid-1), cables))
		if rst1 >= n:
			print(mid)
		else:
			print(mid-1)
		return()
	cnt = sum(map(lambda x:x//mid, cables))
	if cnt >= n:
		binary(mid+1, end)
	elif cnt < n:
		binary(start,mid)
	
if __name__ == '__main__':
	k,n = map(int,read().split())
	cables = [int(read()) for _ in range(k)]
	s = 0
	for i in cables:
		s += i
	cable_length = s // n
	binary(0,cable_length+1)