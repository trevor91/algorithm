# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(200001)
r = lambda: sys.stdin.readline().split()

n, q = map(int, r())
# juin = [-1 for _ in range(2*1000000+1)] #물건 주인 아이디가 들어있음
juin = [-1] * (2*1000000+1)
sangsa = [False]*(n+1)
for _ in range(n):
    t = [int(i) for i in r()]
    sangsa[t[0]] = t[1]
    for i in t[3:]:
        juin[i] = t[0]

find = False
def up(id1, id2):
    global find
    if find==False:
        if id1==id2:
            find = True
        else:
            if sangsa[id2]!=False:
                up(id1, sangsa[id2])

for _ in range(q):
    people1, pro = map(int, r())
    people2 = juin[pro] #자원 주인
    find = False
    up(people1, people2)
    print('true' if find else 'false')