# -*- coding: utf-8 -*-

from sortThreadHandler import *

allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]


def main():
    exitVar = False
    listType = ""
    while not exitVar:
        print("1. Insert Sort")
        print("2. Merge Sort")
        print("3. Heap Sort")
        print("4. RUN ALL! (Run All sorts with all lists!)")
        while True:
            try:
                execType = int(input("Which sorting algo to run? (1-3)"))
                if 4 >= execType > 0:
                    break
            except:
                print("Please type an integer (1-3)")

        if execType != 4:
            print("1. Permutations")
            print("2. Sorted")
            while True:
                try:
                    listsToUse = int(input("Which list to use (1-2)"))
                    if listsToUse == 1:
                        listType = "Perm"
                    elif listsToUse == 2:
                        listType = "Sorted"
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

            if execType == 1:
                if listsToUse == 1:
                    sys.stdout.flush()
                    runAllPermInsert(length, listType)
                elif listsToUse == 2:
                    sys.stdout.flush()
                    runAllSortedInsert(length, listType)
            elif execType == 2:
                if listsToUse == 1:
                    sys.stdout.flush()
                    runAllPermMerge(length, listType)
                elif listsToUse == 2:
                    sys.stdout.flush()
                    runAllSortedMerge(length, listType)
            elif execType == 3:
                if listsToUse == 1:
                    sys.stdout.flush()
                    runAllPermHeap(length, listType)
                elif listsToUse == 2:
                    sys.stdout.flush()
                    runAllSortedHeap(length, listType)

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
        elif execType == 4:
            run_all_sorts()


if __name__ == '__main__':
    main()
