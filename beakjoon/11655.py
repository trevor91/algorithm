# ascii to char, char to ascii : ord, chr
# space 32
# 0 48
# 9 57

# A 65
# Z 90

# a 97
# z 122

import sys
if __name__ == '__main__':
	s = sys.stdin.readline()
	s = [ord(x) for x in s]
	for i, x in enumerate(s):
		if x > 64 and x < 91:
			x += 13
			if x > 90:
				x = x % 91 + 65
			s[i] = x
		elif x > 96 and x < 123:
			x += 13
			if x > 122:
				x = x % 123 + 97
			s[i] = x
	print(''.join([chr(x) for x in s]))