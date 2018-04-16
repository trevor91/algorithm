# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
read = lambda: sys.stdin.readline()

def calc(a,b):
	if a + b == 7:
		return 2
	return 1

def solution(A):
    rst = 0
    for i in range(len(A)):
    	temp = 0
    	standard  = A[i]
    	for j in range(len(A)):
    		if standard == A[j]:
    			continue
    		else:
    			temp += calc(standard,A[j])
    	if rst > temp or rst == 0:
    		rst = temp
    return rst

n = int(read().strip())
arr = [int(x) for x in read().split()]
print(solution())