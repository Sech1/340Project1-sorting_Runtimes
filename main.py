from threading import Thread

from execSortingAndTiming import *
from util import *

allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]
smallPermList = ["15K", "30K", "45K", "60K"]

def main():
    runAllPerm()


def runAllPerm():
    for x in range(len(smallPermList)):
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm, args=(smallPermList[x],))
        spinnerThread = Thread(target=util.spinning_cursor)

        threadAlgo.start()
        spinnerThread.start()
        threadAlgo.join()
        util.go = False


if __name__ == '__main__':
    main()
