#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    description='Convert r,g,b ints into hexadecimals')
parser.add_argument('ints', metavar='N', type=int, nargs='+')

if __name__ == '__main__':
    args = parser.parse_args()
    assert (len(args.ints) == 3)

    hexa = [hex(x) for x in args.ints]
    print("#{0}{1}{2}".format(hexa[0][2:], hexa[1][2:], hexa[2][2:]))
