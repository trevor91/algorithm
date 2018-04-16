import sys
read = lambda: sys.stdin.readline().split()


def solution(A):
	# write your code in Python 3.6
	if len(A) < 2:
		return len(A)
	arr = [-1 for _ in range(len(A))]
	if A[0] > A[1]: arr[0] = 0
	elif A[0] < A[1]:	arr[0] = 1
	for i in range(1, len(A)):
		if A[i] > A[i-1]: arr[i] = 0
		elif A[i] < A[i-1]: arr[i] = 1
	
	length_max = 0
	length = 1
	for i in range(1,len(arr)):
		if(arr[i] == -1):
			if(length_max < length): length_max = length
			length = 1
		else:
			if(arr[i] != arr[i-1]):
				length += 1
			else:
				if A[i-1] > A[i] and A[i] < A[i+1]: length = 2
				elif A[i-1] < A[i] and A[i] > A[i+1]: length = 2
				else: length = 1
			if(length_max < length): length_max = length
	return(length_max)

# a = read()
a = [0,1,1, 1,1, 1,1, 0,1, ]
print(solution(a))