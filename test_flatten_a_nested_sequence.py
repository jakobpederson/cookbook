import unittest

import flatten_a_nested_sequence


class FlattenANestedSequenceTest(unittest.TestCase):

    def setUp(self):
        self.sut = flatten_a_nested_sequence.FlattenANestedSequence()

    def test_x(self):
        lst = [1, [2, [3, 4]]]
        expected = [1, 2, 3, 4]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)

    def test_y(self):
        lst = [1, [2]]
        expected = [1, 2]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)

    def test_r(self):
        lst = [1, 2]
        expected = [1, 2]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)

    def test_a(self):
        lst = [1, [2, [3, [4, ]]]]
        expected = [1, 2, 3, 4]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)

    def test_b(self):
        lst = [1, [2, [3, [4, [[[[[[[5], 6], 7], 8], 9], 10] ]]]]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.sut.flatten(lst)
        print('RESULT:', result)
        self.assertCountEqual(expected, result)

    def test_c(self):
        lst = [1, {2}]
        expected = [1, 2]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)

    def test_d(self):
        lst = [1, "cde"]
        expected = [1, "cde"]
        result = self.sut.flatten(lst)
        self.assertCountEqual(expected, result)
