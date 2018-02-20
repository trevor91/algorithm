import sys
from array import array
read = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	input_cnt = int(read())
	rst = array('l', [1,2,4])
	for i in range(input_cnt):
		num = int(read())
		if len(rst) < num:
			for j in range(len(rst), num):
				temp = rst[j-1]+rst[j-2]+rst[j-3]
				rst.append(temp)
		print(rst[num-1])