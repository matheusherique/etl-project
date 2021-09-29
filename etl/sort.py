class Sort():
    def quicksort(self, a_list):
        self.__quicksort_helper(a_list, 0, len(a_list)-1)

    def __quicksort_helper(self, a_list, first, last):
        if first < last:

            splitpoint = self.__partition(a_list, first, last)

            self.__quicksort_helper(a_list, first, splitpoint-1)
            self.__quicksort_helper(a_list, splitpoint + 1, last)

    def __partition(self, a_list, first, last):
        pivotvalue = a_list[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and a_list[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while a_list[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = a_list[leftmark]
                a_list[leftmark] = a_list[rightmark]
                a_list[rightmark] = temp

        temp = a_list[first]
        a_list[first] = a_list[rightmark]
        a_list[rightmark] = temp

        return rightmark
