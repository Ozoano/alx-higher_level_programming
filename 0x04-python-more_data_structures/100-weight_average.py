#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    total = sum(map(lambda x: x[0] * x[1], my_list))
    num = sum(map(lambda x: x[1], my_list))
    return total / num


if __name__ == '__main__':
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
