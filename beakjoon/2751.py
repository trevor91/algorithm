import sys
r = lambda: sys.stdin.readline()
for i in sorted([int(r()) for _ in range(int(r()))]):
    sys.stdout.write(str(i)+'\n')