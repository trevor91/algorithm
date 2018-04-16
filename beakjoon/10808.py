import sys
import string

def main():
	user_input = sys.stdin.readline().strip()
	for char in string.ascii_lowercase:
		print(user_input.count(char),end = ' ')

if __name__ == '__main__':
	main()