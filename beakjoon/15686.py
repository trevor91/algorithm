import sys
read = lambda:sys.stdin.readline().split()

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def select(hubo, choice):
    if len(choice) == M:
        city_dist(choice)
        return None
    
    for h in hubo:
        if len(choice) > 0 and choice[-1] > h:
            continue
        t = hubo.copy()
        t.remove(h)
        select(t, choice+[h])

def city_dist(index):
    global ans
    ret = 0
    for d in distance:
        l = []
        for i in index:
            l += [d[i]]
        ret += min(l)
    if ans > ret:
        ans = ret

if __name__ == '__main__':
    N, M = map(int, read())
    ans = float('inf')
    home = []
    chicken = []
    for r in range(N):
        row = [int(i) for i in read()]
        for c in range(N):
            if row[c] == 1:
                home.append([r,c])
            elif row[c] == 2:
                chicken.append([r,c])
    distance = [[0 for _ in range(len(chicken))] for _ in range(len(home))]
    for h in range(len(home)):
        for c in range(len(chicken)):
            distance[h][c] = dist(home[h], chicken[c])
    select(list(range(len(chicken))), [])
    print(ans)
