class BuildHeap:
    def __init__(self, input_file):
        self.input_file = input_file

    @classmethod
    def build_Heap(cls, list, n, i):
        largest = i  # Initialize largest val as root
        left = 2 * i + 1
        right = 2 * i + 2

        # See if left child of root exists and is
        # greater than root
        if left < n and list[i] < list[left]:
            largest = left

        # See if right child of root exists and is
        # greater than root
        if right < n and list[largest] < list[right]:
            largest = right

        # Change root, if needed
        if largest != i:
            list[i], list[largest] = list[largest], list[i]  # swap

            # Re-Heapify the root.
            BuildHeap.build_Heap(list, n, largest)
