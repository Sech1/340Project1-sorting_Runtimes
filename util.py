import itertools
import sys


class util:
    go = True

    def __init__(self):
        pass

    @classmethod
    def spinning_cursor(cls):
        spinner = itertools.cycle(['-', '/', '|', '\\'])
        while util.go:
            sys.stdout.write(next(spinner))  # write the next character
            sys.stdout.flush()  # flush stdout buffer (actual character display)
            sys.stdout.write('\b')  # erase the last written char
