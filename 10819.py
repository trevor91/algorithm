import sys

if __name__ == '__main__':
	input_size = int(sys.stdin.readline().strip())
	arr = sys.stdin.readline().split()
	arr = [int(x) for x in arr]
	arr.sort()
	half = input_size // 2
	
	rst = abs(arr[0] - arr[input_size-1])
	if input_size != 3:
		rst += abs(arr[0] - arr[input_size-2])
	
	for i in range(1,half-1):
		rst += abs(arr[i] - arr[input_size-i])
		rst += abs(arr[i] - arr[input_size-i-2])
	
	if input_size % 2 == 0:
		rst += abs(arr[half-1] - arr[half+1])
	else:
		if input_size != 3:
			rst += abs(arr[half-1] - arr[half+2])
		temp1 = abs(arr[half-1] - arr[half])
		temp2 = abs(arr[half+1] - arr[half])
		rst += temp1 if temp1>temp2 else temp2 
	print(rst)