import sys
import bisect
import collections
r = lambda: sys.stdin.readline().split()

def dfs(start):
    if visited[start] == False:
        visited[start] = True
        print(start+1, end=' ')
        for num in link[start]:
            dfs(num)

def bfs(start):
    q = collections.deque()
    q.append(start)

    while q:
        start = q.popleft()
        if visited[start] == False:
            visited[start] = True
            print(start+1, end=' ')
            for num in link[start]:
                if visited[num]==False:
                    q.append(num)

if __name__ == '__main__':
    N, M, V = [int(i) for i in r()]
    link = [[] for n in range(N)]
    for _ in range(M):
        a,b = [int(i) for i in r()]
        a-=1; b-=1
        i = bisect.bisect_left(link[a], b)
        if i == len(link[a]) or b != link[a][i]:
            link[a].insert(i,b)
            i = bisect.bisect_left(link[b], a)
            link[b].insert(i,a)

    #dfs
    visited = [False for _ in range(N)]
    dfs(V-1)
    print()

    #bfs
    visited = [False for _ in range(N)]
    bfs(V-1)
