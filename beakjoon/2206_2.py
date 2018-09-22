import collections, sys
r = lambda: sys.stdin.readline()

def bfs():
    q = collections.deque()
    q.append((0,0,1))
    move_y = [0,0,1,-1]
    move_x = [1,-1,0,0]
    while q:
        y, x, de = q.popleft()
        if y==N-1 and x==M-1:
            return visited[y][x][de]

        for i in range(4):
            next_y, next_x = y+move_y[i], x+move_x[i]
            if 0<= next_y <N and 0<= next_x <M:
                if mat[next_y][next_x] == '1':
                    if de==1:
                        if visited[next_y][next_x][0] == 0:
                            visited[next_y][next_x][0] = visited[y][x][1] + 1
                            q.append((next_y, next_x, 0))
                else:
                    if visited[next_y][next_x][de] == 0:
                        visited[next_y][next_x][de] = visited[y][x][de] + 1
                        q.append((next_y, next_x, de))
    return -1

N,M = map(int,r().split()) #세로, 가로
mat = []
for _ in range(N):
    mat.append(r().strip())
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][1] = 1
print(bfs())