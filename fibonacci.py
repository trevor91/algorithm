import numpy as np
import time

def dynamicFibo(arg):
	if arr[arg] != -1:
		return(arr[arg])
	else:
		arr[arg] = dynamicFibo(arg-1) + dynamicFibo(arg-2)
		return(arr[arg])


def fibo(arg):
	if arg == 0:
		return(0)
	elif arg == 1:
		return(1)
	else:
		return(fibo(arg-1) + fibo(arg-2))


if __name__ == '__main__':
	global arr

	input = 46
	arr = np.full(input+1,-1, dtype = np.int)
	arr[0] = 0
	arr[1] = 1
	
	start = time.time()
	print(dynamicFibo(input))
	print("time : " + str(time.time() - start))

	start = time.time()
	print(fibo(input))
	print("time : " + str(time.time() - start))