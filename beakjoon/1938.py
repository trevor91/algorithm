'''
5개의 동작
상하좌우 턴
BBB의 나무를
EEE로 옭기는 최소 횟수를 구해라.

-> 센터 B의 위치(xy)와 Horizontal가로 , vertical세로 로 표현 -> n by n by 2 행렬로 방문 체크
-> E도 위와 같이 표현

sol 1. 완탐. heapq
'''

import sys
from heapq import heappop, heappush
r = lambda: sys.stdin.readline()


def get_horizontal_vertical(param_list):
    if param_list[0][0] == param_list[1][0]: # y값이 같으면 
        return h #vertical
    return v


def get_center(mat):
    ret_b = []
    ret_e = []

    for y in range(N):
        for x in range(N):
            if mat[y][x] == 'B':
                ret_b.append([y,x])
            elif mat[y][x] == 'E':
                ret_e.append([y,x])

            if len(ret_b) >= 2 and len(ret_e) >= 2:
                break

    ret_b = ret_b[1] + [get_horizontal_vertical(ret_b)] # [y,x,hv]
    ret_e = ret_e[1] + [get_horizontal_vertical(ret_e)]
    return ret_b, ret_e


def is_posible(y,x,hv):
    if hv==h:
        if y>=0 and x>=1 and y<N and x<N-1:
            for i in range(x-1, x+2):
                if mat[y][i]=='1':
                    return False
            return True
    elif hv==v:
        if y>=1 and x>=0 and y<N-1 and x<N: 
            for i in range(y-1, y+2):
                if mat[i][x]=='1':
                    return False
            return True
    return False

def UDLR(B, move_x, move_y): #위 아래 왼쪽 오른쪽
    if is_posible(B[0]+move_y, B[1]+move_x, B[2]):
        return [B[0]+move_y, B[1]+move_x, B[2]]
    return None
    
def T(B):
    #is posible?
    y,x,hv = B
    if y>0 and x>0 and y<N-1 and x<N-1:
        for cur_y in range(y-1, y+2):
            for cur_x in range(x-1, x+2):
                if mat[cur_y][cur_x]=='1':
                    return None
        hv = 0 if hv==1 else 1
    return [y,x,hv]

    
def main():
    global N, mat, h, v
    N = int(r().strip())
    mat = []
    h = 0
    v = 1
    for y in range(N):
        mat.append(r().strip())
    
    #find B, E center
    B, E = get_center(mat) #b, e position
    
    visited = [[[False for _ in range(2)] for _ in range(N)] for _ in range(N)]
    path = []
    heappush(path, (0, B))
    visited[B[0]][B[1]][B[2]] = True
    
    #완탐, 5개의 액션 U,D,L,R,T 위아래좌우턴
    move_x = [0,0,1,-1]
    move_y = [1,-1,0,0]
    while path:
        cnt, cur_B = heappop(path)
        if cur_B == E:
            return cnt
        for m_y, m_x in zip(move_y, move_x): #위 아래 왼쪽 오른쪽
            next_B = UDLR(cur_B, m_y, m_x)
            if next_B != None:
                if visited[next_B[0]][next_B[1]][next_B[2]] == False:
                    visited[next_B[0]][next_B[1]][next_B[2]] = True
                    heappush(path, (cnt+1, next_B))
        t = T(cur_B) #턴
        if t != None:
            if visited[t[0]][t[1]][t[2]] == False:
                visited[t[0]][t[1]][t[2]] = True
                heappush(path, (cnt+1, t))
    return 0

if __name__ == '__main__':
    res = main()
    print(res)