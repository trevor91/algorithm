import sys
r = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
	strings = r().split('-')
	rst = strings[0].split('+')
	calc = 0
	for num in rst:
		calc += int(num)
	rst = calc

	for string in strings[1:]:
		string = string.split('+')
		calc = 0
		for char in string:
			calc += int(char)
		rst -= calc
	print(rst)