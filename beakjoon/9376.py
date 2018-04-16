import sys, re
from heapq import heappush, heappop
read = lambda: sys.stdin.readline()

def check(x,y):
	if x == 0 or y == 0 or x == w-1 or y == w-1:
		return(True)
	return(False)

def go(i):

	while prisoners:
		wall, (cur_x, cur_y) = heappop(prisoners)
		print(wall, (cur_x, cur_y), visited[i])
		if check(cur_x,cur_y):
			return(wall,cur_x,cur_y)
		if i == 1 and (cur_x, cur_y) in visited[0]:
			return(wall,cur_x,cur_y)
		for calc_x, calc_y in zip(move_x, move_y):
			pre_x = calc_x + cur_x
			pre_y = calc_y + cur_y
			if cur_x >= 0 and pre_y >= 0 and pre_x < w and pre_y < h:
				if not (pre_x, pre_y) in visited[i]:
					if (blueprint[pre_y][pre_x] == '.') or (blueprint[pre_y][pre_x] == '$'):
						heappush(prisoners, (wall, (pre_x, pre_y)))
					elif blueprint[pre_y][pre_x] == '#':
						heappush(prisoners, (wall+1, (pre_x, pre_y)))
					visited[i].add((pre_x, pre_y))
if __name__ == '__main__':
	testcase = int(read().strip())
	move_x = [0,0,1,-1]
	move_y = [1,-1,0,0]

	for _ in range(testcase):
		h, w = map(int,read().split())
		blueprint = []
		first_prisoners = []
		prisoners = []
		visited = [set(),set()]
		for i in range(h):
			temp = read().strip()
			blueprint.append([x for x in temp])
			prisoner = [t.start() for t in re.finditer('\$',temp)]
			for j in prisoner:
				first_prisoners.append((0,(j,i)))

		rst = 0
		for i, data in enumerate(first_prisoners):
			heappush(prisoners, data)
			visited[i].add(data[1])
			temp, x, y = go(i)
			if i == 0:
				temp_set = set()
				while True:
					if (x, y) == data[1]:
						break
					for calc_x, calc_y in zip(move_x, move_y):
						if (calc_x + x, calc_y + y) in visited[0]:
							temp_set.add((calc_x + x, calc_y + y))
							print('temp: ' ,temp_set)
				visited[0].intersection_update(temp_set)
			rst += temp
		print(rst)