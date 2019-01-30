import os
import time

from insertionSort import *


# InsertionSort
# MergeSort
# HeapSort

class ExecSortingAndTiming:
    def __init__(self):
        pass

    @classmethod
    def exec_insertion_sort_perm(cls, length):
        count = 0
        list = open('lists/permuted/perm' + length + '.txt').readlines()
        for x in range(0, len(list)):
            list[x] = list[x].strip('\n')

        start = time.time()
        InsertionSort.insertion_sort_algo(list)
        end = time.time()
        for i in range(0, len(list)):
            print(list[i])
            count = count + 1
        print(end - start)
        print(count)