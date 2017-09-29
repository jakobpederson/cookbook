

class FlattenANestedSequence():

    def flatten(self, lst):
        return self.recurs(lst)

        # new_lst = list(lst)
        # result= []
        # for value in new_lst:
        #     if type(value) == list:
        #         for x in value:
        #             if type(x) == list:
        #                 for y in x:
        #                     if type(y) == list:
        #                         print("bottom")
        #                     else:
        #                         result.append(y)
        #             else:
        #                 result.append(x)
        #     else:
        #         result.append(value)
        # return result

    def recurs(self, lst, result=None):
        result = result or []
        for value in lst:
            if type(value) == list:
                self.recurs(value, result)
            else:
                result.append(value)
        return result



