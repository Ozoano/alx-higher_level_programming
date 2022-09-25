#!/usr/bin/python3
def multiple_returns(sentence):
    """
    returns a tuple with string length and first character
    Args:
        sentence - a string
    Returns:
        (lenght, first character)
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]


if __name__ == '__main__':
    l, f = multiple_returns("At School, I learnt C!")
    print("Length: {:d} - First character: {}".format(l, f))
