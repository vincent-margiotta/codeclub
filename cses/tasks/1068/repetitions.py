#!/usr/bin/env python3


from itertools import groupby


def main(sequence: str) -> int:
    grouped = [list(group) for _, group in groupby(sequence)]
    return len(max(grouped, key=len))


if __name__ == '__main__':
    sequence = input()
    print(main(sequence))