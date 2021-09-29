from .sort import Sort


class Transform():

    def concat_lists(self, list_of_lists):
        complete_list = []

        for item in list_of_lists:
            if item is not None:
                complete_list += item

        return complete_list

    def sort_numbers_list(self, alist):
        alist = self.concat_lists(alist)
        Sort().quicksort(alist)
        return alist
