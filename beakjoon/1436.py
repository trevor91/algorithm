import sys
r = lambda: sys.stdin.readline().strip()
if __name__ == '__main__':
	n = int(r())
	num = 665
	index = 0;
	while n!=index:
		num += 1
		if '666' in str(num):
			index +=1
	print(num)