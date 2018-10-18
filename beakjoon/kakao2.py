# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(200000)
r = lambda: sys.stdin.readline().split()

n, q = map(int, r())
proper = {}
buha = {}
#proper = [[] for _ in range(n+1)] # n번 직원 자산
#buha = [[] for _ in range(n+1)] # n번 직원의 부하직원
for _ in range(n):
    t = [int(i) for i in r()]
    if t[1] in buha.keys():
        buha[t[1]].append(t[0])
    else:
        buha[t[1]]=[t[0]]
    proper[t[0]] = t[3:]

find = False
def search(id1, id2):
    global find
    if find==False:
        if id1 in proper.keys() and id2 in proper[id1]:
            find = True
            return
        if id1 in buha.keys():
            for i in buha[id1]:
                search(i, id2)

for _ in range(q):
    people, pro = map(int, r())
    find = False
    search(people, pro)
    print('true' if find else 'false')
