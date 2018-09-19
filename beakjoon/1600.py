import sys
from heapq import heappop, heappush
import queue
r = lambda: sys.stdin.readline()

def iszero(cur_y, cur_x):
    if cur_y>=0 and cur_x>=0 and cur_y<y and cur_x<x:
        if mat[cur_y][cur_x] == 0:
            return True
    return False

monkey_move_x = [0,0,1,-1]
monkey_move_y = [1,-1,0,0]
hours_move_x = [1, 2, 2, 1, -1, -2, -2, -1]
hours_move_y = [-2, -1, 1, 2, 2, 1, -1, -2]
def move(cnt, cur_y, cur_x, isHouse, cur_K):
    if isHouse:
        move_y, move_x = hours_move_y, hours_move_x
        next_k = cur_K - 1
    else:
        move_y, move_x = monkey_move_y, monkey_move_x
        next_k = cur_K
    for m_y, m_x in zip(move_y, move_x):
        next_y = m_y + cur_y
        next_x = m_x + cur_x
        if iszero(next_y, next_x):
            if visited[next_y][next_x] == -1 or visited[next_y][next_x] < next_k:
                visited[next_y][next_x] = next_k
                heappush(q, (cnt+1, next_y, next_x, next_k))
    return None

def main():
    global x, y, visited, mat, q
    K = int(r().strip())
    x, y = [int(i) for i in r().split()]
    mat = []
    for _ in range(y):
        mat.append([int(i)for i in r().split()])

    visited = [[-1 for _ in range(x)] for _ in range(y)]
    visited[0][0] = K
    q = []
    heappush(q, (0, 0, 0, K)) #[y,x,K]

    while q:
        cnt, cur_y, cur_x, cur_K = heappop(q)
        if cur_y == y-1 and cur_x == x-1:
            return cnt

        #상하좌우
        move(cnt, cur_y, cur_x, False, cur_K)

        #말
        if cur_K > 0:
            move(cnt, cur_y, cur_x, True, cur_K)
    return -1

if __name__ == '__main__':
    print(main())