import sys
r = lambda: sys.stdin.readline()
if __name__ == '__main__':
	n = r().strip()
	arr = [int(x) for x in r().split()]
	arr = sorted(arr)
	time = [arr[0]]
	for i in range(1,len(arr)):
		time.append(time[i-1] + arr[i])
	print(sum(time))
