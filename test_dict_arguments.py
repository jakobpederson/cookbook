import unittest
import dict_arguments


class DictArgumentTests(unittest.TestCase):

    def test_basic(self):
        result = dict_arguments.basic_example("high", "pie")
        self.assertEqual(("high", "pie"), result)

    def test_args(self):
        args_as_list = [1, 2, 3, 4]
        result  = dict_arguments.args(*args_as_list)
        self.assertEqual([2, 4, 6, 8], result)


    def test_kwargs(self):
        kwargs_as_dict = {
            "a": "apple",
            "b": "boy",
            "c": "cat"
        }
        result = dict_arguments.kwargs(**kwargs_as_dict)
        self.assertCountEqual([("a", "apple"), ("b", "boy"), ("c", "cat")], result)

    def produce_number(self):
        import random
        return random.randrange(0, 5)

    def test_alternative_to_elifs(self):
        numb = self.produce_number()
        if numb == 0:
            result = 'create'
        elif numb == 1:
            result = 'push'
        elif numb == 2:
            result = 'pull'
        elif numb == 3:
            result = 'rebase'
        else:
            result = 'reset'
        self.assertTrue(result in ['create', 'push', 'pull', 'rebase', 'reset'])
        MAPPING = {
            0: 'create',
            1: 'push',
            2:'pull',
            3:'rebase',
            4: 'reset'
        }
        result_2 = MAPPING[numb]
        self.assertEqual(result, result_2)

