#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            a += 1
    except (TypeError, ValueError):
        pass
    print()
    return a
