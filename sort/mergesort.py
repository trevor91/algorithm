import random

def merge(a):
    if len(a) < 2:
        return a
    center = len(a) // 2
    left = merge(a[:center])
    right = merge(a[center:])

    k = i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i+=1
        else:
            a[k] = right[j]
            j+=1
        k+=1
    a = a[:k]+left[i:]+right[j:]
    return a

if __name__ == '__main__':
    a = list(range(20))
    random.shuffle(a)
    print(a)
    print(merge(a))