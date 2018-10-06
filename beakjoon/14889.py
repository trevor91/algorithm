#itertools.combinations
import sys
r = lambda: sys.stdin.readline()

def calc(select):
    s = 0
    for i in range(len(select)-1):
        for j in range(i,len(select)):
            a, b = select[i], select[j]
            s += mat[a][b] + mat[b][a]
    score.append(s)
    return None

def permu(hubo, select):
    if len(select)==n//2:
        calc(select)
        return None
    t = hubo.copy()
    for i in hubo:
        t.remove(i)
        permu(t, select+[i])

if __name__ == '__main__':
    n = int(r().strip())
    mat=[]
    for _ in range(n):
        mat.append([int(i) for i in r().split()])
    score = []
    permu(list(range(n)),[])
    ans = float('inf')
    for i in range(len(score)//2):
        if ans > abs(score[i] - score[-i-1]):
            ans = abs(score[i] - score[-i-1])
    print(ans)