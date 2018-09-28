import sys
r = lambda:sys.stdin.readline().split()

def dfs(num, d):
    global ans
    if d == depth:
        ans = 1
        return None
    visited[num] = True
    for n in friend[num]:
        if visited[n]==False:
            dfs(n, d+1)
    visited[num] = False

if __name__ == '__main__':
    N,M = map(int,r())
    friend = [[] for _ in range(N)]
    depth = 4
    ans = 0
    for _ in range(M):
        a,b = map(int, r())
        friend[a].append(b)
        friend[b].append(a)

    for start in range(N):
        if ans == 1:
            break
        visited = [False]*N
        dfs(start, 0)
    print(ans)