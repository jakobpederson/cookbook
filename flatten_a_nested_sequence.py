from collections import Iterable

class FlattenANestedSequence():

    def flatten(self, lst):
        return list(self.recurs(lst))

    def recurs(self, lst):
        for value in lst:
            if isinstance(value, Iterable):
                yield from self.recurs(value)
            else:
                yield value

