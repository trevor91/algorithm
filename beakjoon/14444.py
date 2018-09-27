# manacher 알고리즘
import sys
s = ''
for c in sys.stdin.readline().strip():
    s += c+'#'
s = s[:-1]

p = [0 for _ in range(len(s))]
r = -1
k = -1
for i in range(len(s)):
    if i<=r:
        p[i] = min(p[2*k-i], r-i)
    while i-p[i]-1>=0 and i+p[i]+1<len(s) and s[i-p[i]-1] == s[i+p[i]+1]:
        p[i] += 1
    if i+p[i] < r:
        r = i+p[i]
        k = i
res1 = max(p[::2])
res2 = max(p[1::2]+[0])
if res2%2==0:
    res2-=1
print(max(res1+1 if res1!=1 else 1, res2+1))