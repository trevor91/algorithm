import sys

if __name__ == '__main__':
	n = int(sys.stdin.readline().strip())
	input_list = [int(x) for x in range(1,n+1)]
	fac = 1
	for i in input_list:
		fac *= i
	print(' '.join(str(x) for x in input_list))
	for _ in range(fac):
		for i in range(n-1, 0, -1):
			if input_list[i-1] < input_list[i]:
				for j in range(n-1, i-1, -1):
					if input_list[i-1] < input_list[j]:
						input_list[i-1], input_list[j] = input_list[j], input_list[i-1]
						input_list = input_list[:i] + input_list[:i-1:-1]
						print(' '.join(str(x) for x in input_list))
						break
			else:
				continue
			break