

class FlattenANestedSequence():

    def flatten(self, lst):
        return list(self.recurs(lst))

    def recurs(self, lst):
        for value in lst:
            if type(value) == list:
                yield from self.recurs(value)
            else:
                yield value

