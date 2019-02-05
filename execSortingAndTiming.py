from heapSort import *
from insertionSort import *
from mergeSort import *


# InsertionSort
# MergeSort
# HeapSort
# Also lots of repeated code, not stoked, but it works.
class ExecSortingAndTiming:
    def __init__(self):
        pass

    @classmethod
    def exec_insertion_sort_perm(cls, length, listType):
        input_file = open('lists/permuted/perm' + length + '.txt').readlines()
        sort = InsertionSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()

        sort.insertion_sort_algo(sort.input_file)
        end = time.time()
        with open("outfile.txt", "a+") as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

    @classmethod
    def exec_insertion_sort_sorted(cls, length, listType):
        input_file = open('lists/sorted/sorted' + length + '.txt').readlines()
        sort = InsertionSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()
        sort.insertion_sort_algo(sort.input_file)
        end = time.time()
        with open("outfileInsert.txt", "a+") as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

    @classmethod
    def exec_merge_sort_perm(cls, length, listType):
        input_file = open('lists/permuted/perm' + length + '.txt').readlines()
        sort = MergeSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()
        sort.merge_sort_algo(sort.input_file)
        end = time.time()

        with open('outfileMerge.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

    @classmethod
    def exec_merge_sort_sorted(cls, length, listType):
        input_file = open('lists/permuted/perm' + length + '.txt').readlines()
        sort = MergeSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()
        sort.merge_sort_algo(sort.input_file)
        end = time.time()

        with open('outfileMerge.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

    @classmethod
    def exec_heap_sort_sorted(cls, length, listType):
        input_file = open('lists/sorted/sorted' + length + '.txt').readlines()
        sort = HeapSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()
        buildHeapTime = sort.heap_sort_algo(sort.input_file)
        end = time.time()

        with open('outfileHeapSort.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

        with open('outfileBuildHeap.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + " BuildHeap" + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = buildHeapTime
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
            print("\n")

    @classmethod
    def exec_heap_sort_perm(cls, length, listType):
        input_file = open('lists/permuted/perm' + length + '.txt').readlines()
        sort = HeapSort(input_file)
        for x in range(0, len(sort.input_file)):
            sort.input_file[x] = sort.input_file[x].strip('\n')

        start = time.time()
        buildHeapTime = sort.heap_sort_algo(sort.input_file)
        end = time.time()

        with open('outfileHeapSort.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = (end - start)
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
        print("\n")

        with open('outfileBuildHeap.txt', 'a+') as outfile:
            outfile.write("Type: " + listType + " BuildHeap" + "\n")
            outfile.write("Word List Size: " + length + "\n")
            outTime = buildHeapTime
            outfile.write(str(outTime) + "\n")
            outfile.write("--------------------" + "\n")
            outfile.close()
            print("\n")
