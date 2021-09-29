from .sort import Sort

class Transform():

    def concat_lists(self, list_of_lists):
        complete_list = []

        for alist in list_of_lists:
            complete_list+=alist

        return complete_list

    def sort_numbers_list(self, alist):
        alist = self.concat_lists(alist)
        Sort().quicksort(alist)
        return alist



    
