import sys
r = lambda: sys.stdin.readline().strip()
if __name__ == '__main__':
	n = int(r())
	plus = [] # input > 2
	mid = []  # 0, 1
	minus = []# input < 0

	for _ in range(n):
		temp = int(r())
		if temp > 1:
			plus.append(temp)
		elif temp <= -1:
			minus.append(temp)
		else:
			mid.append(temp)
	plus = sorted(plus, reverse =True)
	minus = sorted(minus)
	rst = 0
	for i in range(1, len(plus),2):
		rst += plus[i-1] * plus[i]
	if len(plus) % 2:
		rst += plus[-1]
	
	for i in range(1, len(minus),2):
		rst += minus[i-1] * minus[i]
	if len(minus) % 2:
		if not 0 in mid:
			rst += minus[-1]
	rst += sum(mid)
	print(rst)