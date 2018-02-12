#()로 레이저를 쏘면 진행중인 괄호의 개수를 더하고. )괄호로 막대기가 끝날때마다 +1
import sys

read = lambda: sys.stdin.readline().strip()

def main():
	string = read()
	rst = 0
	progress_bar = 0
	for i, char in enumerate(string):
		if char == "(" and string[i+1] == ")": #laser
			rst += progress_bar
		elif char == ")" and string[i-1] != "(": #end progress bar
			progress_bar -= 1
			rst +=1
		elif char == "(": #start progress bar
			progress_bar += 1
	print(rst)

if __name__ == '__main__':
	main()