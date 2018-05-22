import sys
r = lambda: sys.stdin.readline()

if __name__ == '__main__':
	n = int(r().strip())
	memo = [0 for _ in range(n+1)] #n일까지 일했을때 버는 수익
	for i in range(n):
		add_t, add_p = map(int, r().split())
		memo[i] = max(memo[:i+1])
		if add_t == 1:
			if memo[i+1] < memo[i] + add_p:
				memo[i+1] = memo[i] + add_p
		elif i+add_t <= n and memo[i+add_t] < memo[i] + add_p:
			memo[i+add_t] = memo[i] + add_p
	print(max(memo))