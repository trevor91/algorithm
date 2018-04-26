import sys
r = lambda: sys.stdin.readline().strip()
i = 1
num = 1
if __name__ == '__main__':
	n = int(r())
	while True:
		if(num//10000000):
			if(i+8 <= n):
				i+=8
			else:
				break
		elif(num//1000000):
			if(i+7 <= n):
				i+=7
			else:
				break
		elif(num//100000):
			if(i+6 <= n):
				i+=6
			else:
				break
		elif(num//10000):
			if(i+5 <= n):
				i+=5
			else:
				break
		elif(num//1000):
			if(i+4 <= n):
				i+=4
			else:
				break
		elif(num//100):
			if(i+3 <= n):
				i+=3
			else:
				break
		elif(num//10):
			if(i+2 <= n):
				i+=2
			else:
				break
		else:
			if(i+1 <= n):
				i+=1
			else:
				break
		num+=1
	print(str(num)[n-i])