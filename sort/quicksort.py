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

def quick2(a):
    if len(a) < 2:
        return a
    start = 0
    end = len(a)-1
    pivot = a[(start + end) // 2]
    while start < end:
        if a[start] < pivot:
            start+=1
            continue
        if a[end] > pivot:
            end-=1
            continue
        a[start], a[end] = a[end], a[start]
    return quick2(a[:start]) + [pivot] + quick2(a[start+1:])

if __name__ == '__main__':
    a = list(range(5))
    random.shuffle(a)
    print(a)
    #quick(0, len(a)-1)
    a = quick2(a)
    print(a)