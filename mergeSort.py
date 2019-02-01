class MergeSort:
    def __init__(self, input_file):
        self.input_file = input_file

    @classmethod
    def merge_sort_algo(cls, list):
        if len(list) > 1:
            m = len(list) // 2
            left = list[:m]
            right = list[m:]

            MergeSort.merge_sort_algo(left)
            MergeSort.merge_sort_algo(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i = i + 1
                else:
                    list[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1
