# 0~500,000
import sys
read = lambda: sys.stdin.readline().strip()

def btn_check(string):
	for i, c in enumerate(string):
		if c in btn:
			return(i+1) #1~6
	return(0)

if __name__ == '__main__':
	target = int(read())
	btn_cnt = int(read())
	btn = read().split()
	ch = 100
	cnt = 500000
	for i in range(1000001):
		if target-i >= 0 and not btn_check(str(target-i)):
			cnt = len(str(target-i)) + i
			break
		if not btn_check(str(target+i)):
			cnt = len(str(target+i)) + i
			break

	if abs(target-ch) > cnt:
		print(cnt)
	else:
		print(abs(target-ch))