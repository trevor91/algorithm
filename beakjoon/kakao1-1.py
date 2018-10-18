##최종 제출본

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

#input
r = lambda: sys.stdin.readline().strip()
n = int(r())
d = {}

def set_dict(c, d):
    if len(c)<=0:
        return
    if len(c)==1:
        if c in d.keys():
            d[c].update({'\n':0})
        else:
            d[c] = {'\n':0}
    if not c[0] in d.keys():
        d[c[0]] = {}
    set_dict(c[1:], d[c[0]])

for _ in range(n):
    set_dict(r(), d)

q = int(r())

find = False
def search(c, d):
    global find
    if find==False:    
        if len(c) == 1 and c in d.keys():
            find = d[c]
        if c[0] in d.keys() and len(c)>1:
            search(c[1:], d[c[0]])

def visit(c, d):
    if len(c)==0:
        pass
    elif len(c)==1:
        d[c]['\n'] = 1
    else:
        visit(c[1:], d[c[0]])

add_list1=set()
add_list2=set()
def part(string, d):
    for k in d:
        if k=='\n':
            if d['\n']==1:
                add_list1.add(string)
            else:
                add_list2.add(string)
        else:
            part(string+k, d[k])
#go
for _ in range(q):
    t = r()
    if t[0]=='1':
        s, k = t.split()[1:3]
        k=int(k)
        find=False
        search(s, d)
        add_list1 = set()
        add_list2 = set()
        part(s, find)
        add_list1 = sorted(add_list1)
        add_list2 = sorted(add_list2)
        cnt = 0
        for c in add_list1:
            if cnt>=k:
                break
            cnt+=1
            print(c)

        for c in add_list2:
            if cnt>=k:
                break
            cnt+=1
            print(c)
            if '\n' in find.keys():
                find['\n'] = 1
            visit(c[len(s):],find)
    elif t[0]=='2':
        set_dict(t[2:], d)
        n+=1