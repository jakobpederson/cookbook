import unittest
import dicts


class TestDicts(unittest.TestCase):

    def setUp(self):
        self.a = {
            "one": 1,
            "two": 2,
            "three": 3,
            "a": "apple",
            "b": "blueberry"
        }
        self.b = {
            "a": "apple",
            "b": "blueberry",
            "c": "cherry",
            "d": "durian"
        }

    def test_remove_second_dicts_elements_from_first(self):
        expected = {"one": 1, "two": 2, "three": 3}
        result = dicts.remove_second_from_first(self.a, self.b)
        self.assertEqual(expected, result)
        result = dicts.remove_second_from_first(self.b, self.a)
        expected = {"c": "cherry", "d": "durian"}
        self.assertEqual(expected, result)

    def test_remove_second_dict_keys_from_first_dict_keys(self):
        expected = {"one", "two", "three"}
        result = dicts.remove_second_keys_from_first(self.a, self.b)
        self.assertEqual(expected, result)
        expected = {"c", "d"}
        result = dicts.remove_second_keys_from_first(self.b, self.a)
        self.assertEqual(expected, result)

    def test_get_set_of_tuples_with_second_elements_removed_from_first(self):
        expected = {("one", 1), ("two", 2), ("three", 3)}
        result = dicts.remove_second_items_from_first(self.a, self.b)
        self.assertEqual(expected, result)
        expected = {("c", "cherry"), ("d", "durian")}
        result = dicts.remove_second_items_from_first(self.b, self.a)
        self.assertEqual(expected, result)

    def test_what_does_enumerate_do(self):
        self.c = {
            "pikachu": "electric",
            "charmander": "fire",
            "bulbasaur": "leaf",
            "squirtle": "water"
        }
        for k, v in enumerate(self.c):
            print(k, v)
        self.d = [
            "jigglypuff",
            "wooper",
            "sentret",
            "murkcrow"
        ]
        for k, v in enumerate(self.d):
            print(k, v)
        self.fail('x')
