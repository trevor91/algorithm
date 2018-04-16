import sys
read = lambda: sys.stdin.readline()

if __name__ == '__main__':
	while True:
		i = read().split()
		n = int(i[0])
		if n == 0:
			break
		i = [int(x) for x in i[1:]]
		
		temp = []
		for a in range(n):
			temp.append(a)
			for b in range(a+1,n):
				if b in temp: continue
				temp.append(b)
				for c in range(b+1,n):
					if c in temp: continue
					temp.append(c)
					for d in range(c+1,n):
						if d in temp: continue
						temp.append(d)
						for e in range(d+1,n):
							if e in temp: continue
							temp.append(e)
							for f in range(e+1,n):
								if f in temp: continue
								temp.append(f)
								out = [str(i[x]) for x in temp]
								print(' '.join(out))
								temp.remove(f)
							temp.remove(e)
						temp.remove(d)
					temp.remove(c)
				temp.remove(b)
			temp.remove(a)
		print()