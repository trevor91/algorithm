import sys
read = lambda: sys.stdin.readline()
def gcd(a,b):
	if b == 0:
		return(a)
	return(gcd(b, a%b))
if __name__ == '__main__':
	n = int(read())
	for _ in range(n):
		case = [int(x) for x in read().split()]
		s = 0
		for i in range(1, case[0]+1):
			for j in range(i+1, case[0]+1):
				s += gcd(case[i],case[j])
		print(s)