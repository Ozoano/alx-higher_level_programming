#!/usr/bin/python3
def complex_delete(a_dict, val):
    """
    deletes a value in a dictionary
    """
    if a_dict is None:
        return None
    if a_dict is None:
        return None

    keys = tuple(a_dict.keys())
    for k in keys:
        if a_dict[k] == val:
            del a_dict[k]
    return a_dict


if __name__ == '__main__':
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print(a_dictionary)
    print("--")
    print(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print(a_dictionary)
    print("--")
    print(new_dict)
