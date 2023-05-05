import sys

from calc import xor


def main():
    data = sys.argv[1:]
    try:
        data = list(map(int, data))
    except ValueError:
        print('ERROR: input only integer')
        return 1
    else:
        print(xor(*data))
        return 0


if __name__ == '__main__':
    main()
