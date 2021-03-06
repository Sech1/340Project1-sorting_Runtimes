class InsertionSort:
    def __init__(self, input_file):
        self.input_file = input_file

    @classmethod
    def insertion_sort_algo(cls, list):

        for x in range(1, len(list)):
            # currentVal
            key = list[x]
            # position
            i = x

            while i > 0 and list[i - 1] > key:
                list[i] = list[i - 1]
                i = i - 1

            list[i] = key
