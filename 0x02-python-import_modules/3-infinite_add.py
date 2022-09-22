#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = (sys.argv)
    pops = args.pop(0)
    print(sum(map(int, pops)))
