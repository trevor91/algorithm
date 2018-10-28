import time, random
from heapsort import heapsort
from insertionsort import insertion2
from mergesort import merge
from quicksort import quick2


if __name__ == '__main__':
    a = list(range(500))
    random.shuffle(a)

    func = [heapsort, insertion2, merge, quick2]

    for f in func:
        start_time = time.time()
        f(a)
        print("%s" %(time.time() - start_time))