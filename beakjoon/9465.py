import sys
r = lambda: sys.stdin.readline()

if __name__ == '__main__':
    t = int(r().strip())
    for _ in range(t):
        n = int(r().strip())
        score = []
        for _ in range(2):
            score.append([int(i) for i in r().split()])
        memo = [[0]*n for _ in range(2)]
        memo[0][0] = score[0][0]
        memo[1][0] = score[1][0]
        memo[0][1] = score[0][1] + memo[1][0]
        memo[1][1] = score[1][1] + memo[0][0]
        for x in range(2,n):
            memo[0][x] = max(memo[0][x-2], memo[1][x-2], memo[1][x-1]) + score[0][x]
            memo[1][x] = max(memo[0][x-2], memo[0][x-1], memo[1][x-2]) + score[1][x]
        print(max(memo[0][-1], memo[0][-2], memo[1][-1], memo[1][-2]))