import sys
read =lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	length = int(read())
	input_list = [int(x) for x in read().split()]
	if length == 1:
		rst = [-1]
	for i in range(length-1, 0, -1):
		if input_list[i-1] < input_list[i]:
			for j in range(length-1, i-1, -1):
				if input_list[i-1] < input_list[j]:
					input_list[i-1], input_list[j] = input_list[j], input_list[i-1]
					rst = input_list[:i] + input_list[:i-1:-1]
					break
		else:
			if i == 1:
				rst = [-1]
			continue
		break
	print(' '.join(str(x) for x in rst))