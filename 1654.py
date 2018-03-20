import sys
read = lambda: sys.stdin.readline()
sys.setrecursionlimit(100000)

def binary(start, end):
	global right, rst
	mid = (start+end) // 2
	if mid == 0 or start == end:
		rst = end
		return()
	cnt = sum(map(lambda x:x//mid, cables))
	if cnt > n:
		right = end
		binary(mid+1, end)
	elif cnt < n:
		binary(start,mid)
	else:
		rst = mid

def binary2(start,end):
	global rst, right
	mid = (start+end)//2
	if mid == 0 or start == end: return()
	cnt = sum(map(lambda x:x//mid, cables))
	if cnt == n:
		rst = mid
		binary2(mid+1,end)
	else:
		right = end
		binary2(start,mid)

if __name__ == '__main__':
	k,n = map(int,read().split())
	cables = [int(read()) for _ in range(k)]
	s = 0
	right = 0
	for i in cables:
		s += i
		if i > right:
			right = i
	cable_length = s // n
	rst = 0
	binary(0,cable_length+1)
	binary2(rst,right)

	for i in range(rst,right+1):
		cnt = 0
		for cable in cables:
			cnt += cable // i
		if cnt!=n:
			print(i-1)
			break
	else:
		print(i)