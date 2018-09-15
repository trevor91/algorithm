import sys
r = lambda : sys.stdin.readline()
sys.setrecursionlimit(10000000)

def sink(mat, height):
	ret = []
	for row in mat:
		ret.append([1 if height < val else 0 for val in row])
	return ret

move_x = [1,-1,0,0]
move_y = [0,0,1,-1]
def propagation(mat, y, x):
	mat[y][x] = 0
	for i in range(4):
		after_y = y+move_y[i]
		after_x = x+move_x[i]
		if after_x>=0 and after_y>=0 and after_x<n and after_y<n:
			if mat[after_y][after_x] == 1:
				mat = propagation(mat, after_y, after_x)
	return mat

def no_sink_area(mat):
	ret = 0
	for y in range(n):
		for x in range(n):
			#propagation
			if mat[y][x] == 1:
				mat = propagation(mat,y,x)
				ret += 1
	return ret

def main():
	global n, ans
	n = int(r().strip())
	mat = []
	_max = 0
	for _ in range(n):
		mat.append([int(i) for i in r().split()])
		temp = max(mat[-1])
		if temp > _max:
			_max = temp

	ans = 0
	for i in range(_max):
		temp_mat = sink(mat, i)
		cnt = no_sink_area(temp_mat)
		if cnt > ans:
			ans = cnt

if __name__ == '__main__':
	main()
	print(ans)