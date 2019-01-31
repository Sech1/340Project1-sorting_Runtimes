# -*- coding: utf-8 -*-

from threading import Thread

from execSortingAndTiming import *
from util import *
import sys

allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]


def main():
    exitVar = False

    while not exitVar:
        print("1. Insert Sort")
        print("2. Merge Sort")
        print("3. Heap Sort")
        while True:
            try:
                exec = int(input("Which sorting algo to run? (1-3)"))
                if 3 >= exec > 0:
                    break
            except:
                print("Please type an integer (1-3)")

        print("1. Permutations")
        print("2. Sorted")
        while True:
            try:
                listsToUse = int(input("Which list to use (1-2)"))
                if 2 >= listsToUse > 0:
                    break
            except:
                print("Please type an integer (1-2)")

        print("1. 15K")
        print("2. 30K")
        print("3. 45K")
        print("4. 60K")
        print("5. 75K")
        print("6. 90K")
        print("7. 105K")
        print("8. 120K")
        print("9. 135")
        print("10. 150K")
        print("11. RUN ALL")
        while True:
            try:
                length = int(input("Which size to run? (1-11)"))
                if 11 >= length > 0:
                    break
            except:
                print("Please type an integer (1-11)")

        if exec == 1:
            if listsToUse == 1:
                sys.stdout.flush()
                runAllPerm(length)

        print("Exit? \n")
        while True:
            try:
                exitInput = int(input("1. Yes \n2. No\n"))
                if exitInput == 1:
                    exitVar = True
                    break
                elif exitInput == 2:
                    break
            except:
                print("Please type and integer (1,2)")


def runAllPerm(count):
    util.go = True
    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    if count < 11:
        threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm, args=(allPermList[count - 1],))
        threadAlgo.start()
        threadAlgo.join()
    elif count == 11:
        for x in range(len(allPermList)):
            threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm, args=(allPermList[x],))
            threadAlgo.start()
            threadAlgo.join()

    util.go = False
    spinnerThread.join()


if __name__ == '__main__':
    main()
