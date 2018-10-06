import sys
r = lambda: sys.stdin.readline().split()

if __name__ == '__main__':
    n,m = map(int, r())
    mat =[]
    for _ in range(n):
        mat.append([[int(i),0,0] for i in r()])
    move_y=[0,1]
    move_x=[1,0]
    ans = 0
    for y in range(n):
        for x in range(m):
            for move in range(2):
                cur_y = y+move_y[move]
                cur_x = x+move_x[move]
                if cur_y<n and cur_x<m:
                    mat[y][x][move+1] = mat[y][x][0]+mat[cur_y][cur_x][0]
    for y in range(n):
        for x in range(m):
            if x+2 < m:
                ans = max(ans, mat[y][x][1]+max(mat[y][x+2][1:])) #ㅡ,ㄱ
                if y-1 >=0:
                    ans = max(ans, mat[y][x][1]+mat[y][x+2][0]+mat[y-1][x+1][0]) # ㅗ
                    ans = max(ans, mat[y][x][1]+mat[y-1][x+2][2]) # ┘
            if y+1 < n:
                ans = max(ans, mat[y][x][1]+max(mat[y+1][x][1:])) #ㅁ,┌
                if x+2 < m: ans = max(ans, mat[y][x][1]+mat[y+1][x+1][0]+mat[y][x+2][0]) #ㅜ
                if x+1 < m: 
                    ans = max(ans, mat[y][x][2]+mat[y+1][x+1][2])
                    ans = max(ans, mat[y][x][1]+mat[y+1][x+1][2])
                    ans = max(ans, mat[y][x][2]+mat[y+1][x+1][1])
                if x-1 >=0: ans = max(ans, mat[y][x][2]+mat[y+1][x-1][2])
            if x+1 < m:
                ans = max(ans, mat[y][x][2]+mat[y][x+1][1]) #┌
                if y+2 < n: ans = max(ans, mat[y][x][2]+mat[y+1][x+1][0]+mat[y+2][x][0]) #ㅏ
                if y-1 >=0: ans = max(ans, mat[y][x][1]+mat[y-1][x+1][1]) #z 180
                if y+1 < n: ans = max(ans, mat[y][x][1]+mat[y+1][x+1][1]) # z
            if y+2 < n:
                ans = max(ans, mat[y][x][2]+max(mat[y+2][x][1:]))
                if x-1 >=0:
                    ans = max(ans, mat[y][x][2]+mat[y+2][x][0]+mat[y+1][x-1][0]) # ㅓ
                    ans = max(ans, mat[y][x][2]+mat[y+2][x-1][1]) # ┘
    print(ans)