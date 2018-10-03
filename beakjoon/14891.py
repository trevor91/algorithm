import sys
r = lambda: sys.stdin.readline()

def spin(a,b, isspin, finish):
    head[a] = (head[a]-b)%8
    finish[a] = True
    if a>0: #1,2,3 -> left
        if isspin[a-1] and finish[a-1]==False:
            spin(a-1, -b, isspin, finish)
    if a<3: #0,1,2
        if isspin[a] and finish[a+1]==False:
            spin(a+1, -b, isspin, finish)

def go(a,b):
    isspin = [False]*3
    for i in range(3):
        left = (head[i]+2)%8
        right = (head[i+1]+6)%8
        if cir[i][left] != cir[i+1][right]:
            isspin[i] = True
    spin(a-1,b, isspin, [False]*4)

if __name__ == '__main__':
    cir = []
    for _ in range(4):
        cir.append([int(i) for i in r().strip()])
    head = [0,0,0,0]
    for _ in range(int(r().strip())):
        a,b = map(int, r().split())
        go(a,b)
    ans = 0
    for i, h in enumerate(head):
        if cir[i][h] == 1:
            ans += 2**i
    print(ans)