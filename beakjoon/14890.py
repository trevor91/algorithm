import sys
r = lambda: sys.stdin.readline().split()

def is_same(a,b):
    if type(a)==int:
        return True if a==b else False
    else:
        for v in a:
            if v!=b:
                return False
        return True

def check_range(v):
    return True if 0<=v<n else False

def check_row(param_list):
    build = [False]*n
    i = 1
    while i < n:
        if is_same(param_list[i], param_list[i-1]):
            i+=1
        elif abs(param_list[i]-param_list[i-1]) > 1:
            return False
        else: #1차이 나는경우
            if param_list[i-1] < param_list[i]: #오르막
                if check_range(i-l):
                    if is_same(param_list[i-l:i-1], param_list[i-1]):
                        if any(build[i-l:i]) == False:
                            for idx in range(i-l,i):
                                build[idx] = True
                            i+=1
                            continue
                return False
            else: #내리막
                if check_range(i+l-1):
                    if is_same(param_list[i+1:i+l], param_list[i]):
                        if any(build[i:i+l]) == False:
                            for idx in range(i, i+l):
                                build[idx] = True
                            i+=1
                            continue
                return False
    return True

if __name__ == '__main__':
    n, l = map(int, r())
    mat = []
    for _ in range(n):
        mat.append([int(i) for i in r()])
    ans = 0
    for row in range(n):
        ans += check_row(mat[row])
    for col in range(n):
        ans += check_row([mat[i][col] for i in range(n)])
    print(ans)