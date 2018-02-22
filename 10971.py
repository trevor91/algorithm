import sys
read = lambda: sys.stdin.readline()

def next_perm(param_list):
	# next permutation
	n = len(param_list)
	for i in range(n-1, 0, -1):
		if param_list[i-1] < param_list[i]:
			for j in range(n-1, i-1, -1):
				if param_list[i-1] < param_list[j]:
					param_list[i-1], param_list[j] = param_list[j], param_list[i-1]
					param_list = param_list[:i] + param_list[:i-1:-1]
					return(param_list)
		else:
			continue
		break
	return(False)

if __name__ == '__main__':
	n = int(read())
	mat = []
	for _ in range(n):
		temp = read().split()
		temp = [int(x) for x in temp]
		mat.append(temp)
	
	path = [x for x in range(0,n)]
	rst = 10000000
	loop = 1
	for i in range(2,n):
		loop *= i
	for _ in range(loop):
		cost = 0
		for i in range(1,n):
			start = path[i-1]
			end = path[i]
			temp = mat[start][end]
			if temp == 0:
				cost += 99999999
				break
			else:
				cost += temp
		cost = cost + mat[path[-1]][path[0]]
		if cost < rst:
			rst = cost
		path = next_perm(path)
	print(rst)