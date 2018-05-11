import sys
r = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	n = int(r())
	arr = []
	for _ in range(n):
		arr.append([int(x)-1 for x in r()])
	positive = []
	for i in range(n):
		for j in range(n):
			if arr[i][j] == 0:
				positive.append([i,j])
	
	move_x = [0,0,1,-1]
	move_y = [1,-1,0,0]
	aptNum = 0
	aptCnt = {}
	while positive:
		aptNum += 1
		y,x = positive.pop()
		arr[y][x] = aptNum
		aptCnt[aptNum] = 1
		
		mini_positive = [[y,x]]
		while mini_positive:
			mini_y, mini_x = mini_positive.pop()
			for temp_y, temp_x in zip(move_y, move_x):
				temp_y += mini_y
				temp_x += mini_x
				if temp_x<0 or temp_y<0 or temp_y>=n or temp_x>=n:
					continue
				if arr[temp_y][temp_x] == 0:
					arr[temp_y][temp_x] = aptNum
					aptCnt[aptNum] += 1
					mini_positive.append([temp_y, temp_x])
					positive.remove([temp_y, temp_x])
	print(aptNum)
	for cnt in sorted(aptCnt.values()):
		print(cnt)