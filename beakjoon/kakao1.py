# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, bisect

#input
r = lambda: sys.stdin.readline().strip()
n = int(r())
d = [] #dict
recommand = [False]*n
for _ in range(n):
    d.append(r())
d.sort()
q = int(r())

#go
my_range = []
cnt = 0
def check_range(ch, param_check_idx, param_start_idx, param_end_idx):
    global my_range
    if param_check_idx == len(ch):
        my_range = [param_start_idx, param_end_idx]
        return
    start = -1
    end = -1
    for i in range(param_start_idx, param_end_idx):
        if param_check_idx >= len(d[i]):
            continue
        if d[i][param_check_idx]==ch[param_check_idx] and start==-1:
            start=i
        elif start!=-1 and d[i][param_check_idx]!=ch[param_check_idx]:
            end=i
            break
        end=i+1
    if start != -1:
        check_range(ch, param_check_idx+1, start, end)

for _ in range(q):
    t = r()
    if t[0]=='1':
        my_range=[]
        s, k = t.split()[1:3]
        k=int(k)
        cnt = 0
        check_range(s,0,0,n)
        cnt = 0
        visited = []
        for i in range(my_range[0], my_range[1]):
            if cnt>=k:
                break
            if recommand[i]==True:
                print(d[i])
                cnt+=1
            else:
                visited.append(i)
        else:
            for i in visited:
                if cnt>=k:
                    break
                print(d[i])
                recommand[i]=True
                cnt+=1
        
    elif t[0]=='2':
        idx = bisect.bisect_left(d, t[2:])
        d.insert(idx, t[2:])
        recommand.insert(idx,False)
        n+=1