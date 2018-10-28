import random

def insertion(a):
    for target_idx in range(1,len(a)):
        change_idx = target_idx
        while change_idx > 0:
            change_idx-=1
            if a[target_idx] > a[change_idx]:
                change_idx+=1
                break
        if a[target_idx] < a[change_idx]:
            temp = a[target_idx]
            for i in range(target_idx, change_idx, -1):
                a[i] = a[i-1]
            a[change_idx] = temp
    return None

def insertion2(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
    return None

if __name__ == '__main__':
    a = list(range(50))
    random.shuffle(a)
    print(a)
    insertion2(a)
    print(a)