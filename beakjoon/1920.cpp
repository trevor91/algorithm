import sys
r = lambda: sys.stdin.readline()

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False

	while first<=last and not found:
		mid = (first+last)//2
		if alist[mid] == item:
			found = True
		else:
			if item<alist[mid]:
				last = mid-1
			else:
				first = mid+1
	return found

if __name__ == '__main__':
	n = int(r().strip())
	arr = [int(x) for x in r().split()]
	arr = sorted(arr)
	m = int(r().strip())
	arr2 = [int(x) for x in r().split()]
	for x in arr2:
		if binarySearch(arr,x):
			print(1)
		else:
			print(0)