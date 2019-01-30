# -*- coding: utf-8 -*-

from threading import Thread

from execSortingAndTiming import *
from util import *

allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]
smallPermList = ["15K", "30K", "45K", "60K"]
testPermList = ["15K"]


def main():
    runAllPerm()


def runAllPerm():
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    for x in range(len(testPermList)):
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm, args=(testPermList[x],))

        threadAlgo.start()
        threadAlgo.join()

    util.go = False
    spinnerThread.join()


if __name__ == '__main__':
    main()
