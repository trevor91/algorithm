import sys
r = lambda: sys.stdin.readline()

def su(a,b): return a+b
def mi(a,b): return a-b
def mul(a,b): return a*b
def di(a,b): return -(abs(a)//abs(b)) if (a<0 or b<0) else a//b
def calc(cnt, ret, param_i):
    global arr, res_max, res_min
    if param_i == N:
        if ret > res_max: res_max = ret
        if ret < res_min: res_min = ret
        return None
    for i in range(4):
        if cnt[i]>0:
            temp_cnt = cnt.copy()
            temp_cnt[i]-=1
            calc(temp_cnt, meth[i](ret, arr[param_i]), param_i+1)

if __name__ == '__main__':
    N = int(r().strip())
    arr = [int(i) for i in r().split()]
    cnt = [int(i) for i in r().split()]
    res_max = -float('inf')
    res_min = float('inf')
    meth = [su, mi, mul, di]
    calc(cnt, arr[0], 1)
    print(res_max, res_min)