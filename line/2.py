#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
move_x = [0,-1,0,1] #남서북동
move_y = [1,0,-1,0]
if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    mat = [[[0,0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        split = sys.stdin.readline().strip().split(' ')
        for j in range(len(split)):
            mat[i][j][0] = split[j][0]
            mat[i][j][1] = int(split[j][1])
    visited = [[[] for _ in range(N)] for _ in range(N)]
    start = [0,0] # y,x
    direc = 0
    while True:
        if mat[start[0]][start[1]][0] in visited[start[0]][start[1]]:
            print(start[1], start[0])
            break
        visited[start[0]][start[1]].append(mat[start[0]][start[1]][0])
        d, dis = mat[start[0]][start[1]] # 방향, 거리
        add_dir = ['F', 'R', 'B', 'L'].index(d)
        direc = (direc + add_dir) % 4
        start[0] = start[0] + (move_y[direc] * dis)
        start[1] = start[1] + (move_x[direc] * dis)

        