from sys import stdin
if __name__ == '__main__':
	n = int(stdin.readline().strip())
	rst = 1
	for i in range(2,n+1):
		rst *= i
	print(rst)