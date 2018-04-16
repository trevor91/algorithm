import sys
read = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	cnt = int(read())
	for _ in range(cnt):
		rst = 0
		stack = []
		line = read()
		if len(line) % 2 != 0:
			print("NO")
			continue
		for char in line:
			if char == "(":
				stack.append(1)
			elif char == ")":
				if len(stack):
					stack.pop()
				else:
					print("NO")
					rst = 1
					break
		if rst == 0:
			if len(stack):
				print("NO")
			else:
				print("YES")