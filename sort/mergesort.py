import random

def merge(a):
    if len(a) < 2:
        return a
    center = len(a) // 2
    left = merge(a[:center])
    right = merge(a[center:])

    i = j = 0
    ret = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i+=1
        else:
            ret.append(right[j])
            j+=1
    ret += left[i:] + right[j:]
    return ret

if __name__ == '__main__':
    a = list(range(5))
    random.shuffle(a)
    print(a)
    print(merge(a))