from threading import Thread

from execSortingAndTiming import *
from util import *

threadAlgo = Thread(target=ExecSortingAndTiming.exec_insertion_sort_perm, args=("30K",))
spinnerThread = Thread(target=util.spinning_cursor)

threadAlgo.start()
spinnerThread.start()
threadAlgo.join()
util.go = False