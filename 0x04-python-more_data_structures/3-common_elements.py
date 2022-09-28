#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets
    Args:
        set_1 - first set element
        set_2 - second set element
    Return:
        common element
    """
    result = [i for i in set_1 if i in set_2]
    return result


if __name__ == '__main__':

    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
