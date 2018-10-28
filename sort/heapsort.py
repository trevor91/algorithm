import random

def left_child(i):
    return i*2+1
def right_child(i):
    return i*2+2
def parent(i):
    return (i-1)//2

def make_heap_tree(a): #min heap
    for i in range(1, len(a)):
        parent_idx = parent(i)
        while parent_idx>-1 and a[i] < a[parent_idx]:
            a[i], a[parent_idx] = a[parent_idx], a[i]
            i = parent_idx
            parent_idx = parent(i)

def pop_heap_tree(a):
    for i in range(len(a)-1, -1, -1):
        yield a[0]
        a[0] = a[i]

        j=0
        l = left_child(j)
        r = right_child(j)
        while (l<=i and a[j] > a[l]) or (r<=i and a[j] > a[r]):
            if a[l] > a[r]:
                a[j], a[r] = a[r], a[j]
                j = r
            else:
                a[l], a[j] = a[j], a[l]
                j = l
            l = left_child(j)
            r = right_child(j)

def heapsort(a):
    make_heap_tree(a)
    return pop_heap_tree(a)

if __name__ == '__main__':
    a = list(range(25))
    random.shuffle(a)
    print(a)
    gener = heapsort(a)
    for v in gener:
        print(v, end= ' ')