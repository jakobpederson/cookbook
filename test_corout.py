import unittest
import corout


class CoroutTests(unittest.TestCase):

    def test_x(self):
        coro = corout.method()
        result = coro.send(1)
        self.fail('x')

    def test_wrapper_add_17(self):
        x = corout.get_number()
        print(x)
        self.assertTrue(x >= 17 and x < 26)

