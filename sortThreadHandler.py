from threading import Thread

from execSortingAndTiming import *
from util import *


# I'm not too stoked with this repeated code, but this was the easiest way to do this at the time.
# Just a side note for myself
class SortThreadHandler:
    allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]

    def __init__(self):
        pass


def runAllPermInsert(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm,
                            args=(SortThreadHandler.allPermList[count - 1], listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def runAllSortedInsert(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_sorted,
                            args=(SortThreadHandler.allPermList[count - 1],
                                  listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_sorted,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def runAllPermMerge(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_merge_sort_perm,
                            args=(SortThreadHandler.allPermList[count - 1],
                                  listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def runAllSortedMerge(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_merge_sort_sorted,
                            args=(SortThreadHandler.allPermList[count - 1],
                                  listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_sorted,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def runAllPermHeap(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_heap_sort_perm,
                            args=(SortThreadHandler.allPermList[count - 1],
                                  listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_heap_sort_perm,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def runAllSortedHeap(count, listType):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_heap_sort_perm,
                            args=(SortThreadHandler.allPermList[count - 1],
                                  listType,))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(SortThreadHandler.allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_heap_sort_perm,
                                args=(SortThreadHandler.allPermList[x], listType,))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


def run_all_sorts():
    print("Starting Insertion Sort: (Sorted)\n")
    runAllSortedInsert(11, "Sorted")
    print("Starting Insertion Sort: (Perm)\n")
    runAllPermInsert(11, "Perm")
    print("Starting Merge Sort: (Sorted)\n")
    runAllSortedMerge(11, "Sorted")
    print("Starting Merge Sort: (Perm)\n")
    runAllPermMerge(11, "Perm")
    print("Starting Heap Sort: (Sorted)\n")
    runAllSortedHeap(11, "Sorted")
    print("Starting Heap Sort: (Perm)\n")
    runAllPermHeap(11, "Perm")
    print("\n")
    print("Done! ")
