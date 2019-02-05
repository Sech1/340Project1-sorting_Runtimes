import time

from buildHeap import *


class HeapSort:
    heapifyTime = 0

    def __init__(self, input_file):
        self.input_file = input_file

    @classmethod
    def heap_sort_algo(cls, list):
        HeapSort.heapifyTime = 0
        n = len(list)

        # Build a maxheap.
        for i in range(n, -1, -1):
            start = time.time()
            BuildHeap.build_Heap(list, n, i)
            end = time.time()
            HeapSort.heapifyTime += (end - start)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            list[i], list[0] = list[0], list[i]  # swap
            start1 = time.time()
            BuildHeap.build_Heap(list, i, 0)
            end1 = time.time()
            HeapSort.heapifyTime += (end1 - start1)

        return HeapSort.heapifyTime
