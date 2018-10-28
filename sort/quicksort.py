import random

def quick(start, end):
    s,e=start,end
    if start >= end:
        return
    pivot = a[(start + end) // 2]
    while start < end:
        if a[start] < pivot:
            start+=1
            continue
        if a[end] > pivot:
            end-=1
            continue
        a[start], a[end] = a[end], a[start]
    quick(s,start-1)
    quick(start+1, e)

if __name__ == '__main__':
    a = list(range(100))
    random.shuffle(a)
    print(a)
    quick(0, len(a)-1)
    print(a)