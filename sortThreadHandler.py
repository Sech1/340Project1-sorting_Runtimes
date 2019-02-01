from threading import Thread

from execSortingAndTiming import *
from util import *


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
                                args=(SortThreadHandler.allPermList[x],))
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
                                args=(SortThreadHandler.allPermList[x],))
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
                                args=(SortThreadHandler.allPermList[x],))
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
                                args=(SortThreadHandler.allPermList[x],))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()
