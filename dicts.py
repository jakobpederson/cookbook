def remove_second_from_first(first, second):
    return {key: first[key] for key in remove_second_keys_from_first(first, second)}


def remove_second_keys_from_first(first, second):
    return first.keys() - second.keys()


def remove_second_items_from_first(first, second):
    return first.items() - second.items()


def enumerate_dict(dict_a):
    enum = enumerate(dict_a)
    return enum
