class Sort():

    def quicksort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return self.__quicksort(array, begin, end)

    def __quicksort(self, array, begin, end):
        if begin >= end:
            return
        pivot = self.__partition(array, begin, end)
        self.__quicksort(array, begin, pivot-1)
        self.__quicksort(array, pivot+1, end)

    def __partition(self, array, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot
