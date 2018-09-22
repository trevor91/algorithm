#0번은 북쪽이니 서쪽을 바라보게.
#1번은 동쪽이니 북쪽을 바라보게.
#2번은 남쪽이니 동쪽을 바라보게.
#3번은 서쪽이니 남쪽을 바라보게.
import sys
r = lambda: list(map(int,sys.stdin.readline().split()))

move_y = [0, -1, 0, 1]
move_x = [-1, 0, 1, 0]
def main(y, x, d):
    ans = 0
    while True:
        if mat[y][x]==no_clean:
            mat[y][x]=clean
            ans += 1

        for i in range(4):
            check_y = y+move_y[d]
            check_x = x+move_x[d]
            d = d-1 if d>0 else 3
            if mat[check_y][check_x] == no_clean:
                y, x = check_y, check_x
                break
            if i==3:
                check_y = y+move_y[(d-1)%4]
                check_x = x+move_x[(d-1)%4]
                if mat[check_y][check_x]==wall:
                    return ans
                y, x = check_y, check_x

if __name__ == '__main__':
    N, M = r()
    y, x, d = r()
    mat = []
    for _ in range(N):
        mat.append(r())
    no_clean, wall, clean = 0, 1, 2
    print(main(y,x,d))