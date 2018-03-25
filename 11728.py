import sys
from array import array
read = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
	n,m = map(int,read())
	a = array('l',map(int,read()))
	b = array('l',map(int,read()))
	rst = array('l',[0]*(n+m))
	pointA=0
	pointB=0
	pointRst=0
	while pointA<n and pointB<m:
		if a[pointA] > b[pointB]:
			rst[pointRst] = b[pointB]
			pointB+=1
		else:
			rst[pointRst] = a[pointA]
			pointA+=1
		pointRst+=1
	print(*(rst[:pointRst]+a[pointA:]+b[pointB:]),sep=' ')
