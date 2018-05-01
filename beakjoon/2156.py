import sys
r = lambda: sys.stdin.readline().strip()
if __name__ == '__main__':
	n = int(r())
	arr = [int(r()) for _ in range(n)]

	memo = [[0]*2 for _ in range(n+1)]
	memo[1][0]=arr[0]
	if(n==1):
		print(arr[0])
	else:
		memo[2][0]=arr[1]
		memo[2][1]=arr[1]+memo[1][0]
		for i in range(3,n+1):
			memo[i][0] = max(memo[i-2][0],memo[i-2][1],memo[i-3][1]) + arr[i-1]
			memo[i][1] = memo[i-1][0] + arr[i-1]
		print(max(memo[n][0],memo[n][1],memo[n-1][1]))