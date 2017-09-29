from collections import Iterable

class FlattenANestedSequence():

    def flatten(self, lst):
        return list(self.recurs(lst))

    def recurs(self, lst):
        print(lst)
        for value in lst:
            if isinstance(value, Iterable) and type(value) not in (str, bytes):
                yield from self.recurs(value)
            else:
                yield value

