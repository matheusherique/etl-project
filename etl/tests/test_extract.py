from django.test import TestCase
from ..extract import Extract


class ExtractTestCase(TestCase):

    def test_get_numbers_list(self):
        first_element = 0.4181707133672159
        last_element = 0.2761236121962305
        numbers_list = Extract(times=10001).get_number_list()

        self.assertEqual(numbers_list[0][0], first_element)
        self.assertEqual(numbers_list[1][-1], last_element)
        self.assertEqual(len(numbers_list), 10000)
