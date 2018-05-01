import sys
if __name__ == '__main__':
	n,m,k = map(int,sys.stdin.readline().split())
	if n+1 < m+k or m*n < n or (m==1 and k!=n) or (k==1 and m!=n):
		print(-1)
	else:
		arr = range(1, n+1)
		rst = list(range(1, m+1))
		while n != m:
			cnt = n - m+1
			if cnt > k:
				cnt = k
			rst[m-1] = sorted(arr[-cnt:], reverse=True)
			arr = arr[:-cnt]
			n -= cnt
			m -= 1
		for i in rst:
			if type(i) == list:
				for j in i:
					sys.stdout.write(str(j)+' ')
			else:
				sys.stdout.write(str(i)+' ')