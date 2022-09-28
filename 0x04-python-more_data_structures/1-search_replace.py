#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_copy = my_list[:]
    my_copy = [x if x != search else replace for x in my_copy]
    return my_copy
