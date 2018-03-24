import sys
read = lambda: sys.stdin.readline()
write = lambda x: sys.stdout.write(x)

def search(target):
	cnt = 0
	for x in range(target,-1,-1):
		if card[x] == card[target]:cnt+=1
		else:break
	for x in range(target+1, n):
		if card[x] == card[target]:cnt+=1
	write(str(cnt))

def binarySearch(start, end, target):
	mid = (start+end)//2
	if end-start < 2:
		if card[start] == target: search(start)
		elif end < n and card[end] == target: search(end)
		else: write('0')
		return()
	else:
		if card[mid] == target:
			search(mid)
			return()
		elif card[mid] > target:
			binarySearch(start,mid,target)
		elif card[mid] < target:
			binarySearch(mid+1,end,target)

if __name__ == '__main__':
	n = int(read().strip())
	card = read().split()
	card = [int(x) for x in card]
	card.sort()
	read()
	target = read().split()
	target = [int(x) for x in target]
	for x in target:
		binarySearch(0, n-1, x)
		write(' ')
	write('\n')