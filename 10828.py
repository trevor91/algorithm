import sys
read = lambda: sys.stdin.readline().strip()
def main():
	#push pop size empty top
	cnt = int(read())
	stack = []
	for i in range(cnt):
		cont = read()
		# print(cont)
		if cont == "top":
			if len(stack):
				print(stack[-1])
			else:
				print("-1")
		elif cont == "pop":
			if len(stack):
				print(stack.pop())
			else:
				print("-1")
		elif cont == "size":
			print(len(stack))
		elif cont == "empty":
			if len(stack) == 0:
				print("1")
			else:
				print("0")
		elif "push" in cont:
			stack.append(int(cont[5:]))

if __name__ == '__main__':
	main()