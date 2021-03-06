from django.test import TestCase
from ..transform import Transform


class TransformTestCase(TestCase):
    def test_concat_lists(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        list_of_lists = Transform().concat_lists(list_of_lists)

        self.assertEqual(list_of_lists, alist)

        list_of_lists = [[1, 2, 3], [4, 5, 6], None]
        alist = [1, 2, 3, 4, 5, 6]

        list_of_lists = Transform().concat_lists(list_of_lists)

        self.assertEqual(list_of_lists, alist)

    def test_sort_numbers_list(self):
        list_of_lists = [[3, 2, 1], [9, 7, 8], [5, 6, 4]]
        alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        list_of_lists = Transform().sort_numbers_list(list_of_lists)

        self.assertEqual(list_of_lists, alist)
