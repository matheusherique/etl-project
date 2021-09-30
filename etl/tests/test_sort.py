from django.test import TestCase
from ..sort import Sort


class SortTestCase(TestCase):
    def test_quicksort(self):
        alist = [9, 3, 4, 2, 6, 7, 5, 1, 8, 0]
        sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Sort().quicksort(alist)

        self.assertEqual(alist, sorted_list)
