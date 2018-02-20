# 1 ≤ E ≤ 15
# 1 ≤ S ≤ 28
# 1 ≤ M ≤ 19

# 7981에서 다시 1 1 1

import sys

if __name__ == '__main__':
	temp = sys.stdin.readline().split()
	E, S, M  = [int(x) for x in temp]
	e, s, m = [1,1,1]
	for i in range(1, 7981):
		if e==E and s==S and m==M:
			print(i)
			break
		e+=1
		s+=1
		m+=1
		if e==16:
			e = 1
		if s==29:
			s = 1
		if m==20:
			m = 1
