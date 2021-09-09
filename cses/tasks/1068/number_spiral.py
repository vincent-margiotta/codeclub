#!/usr/bin/env python3

def main(y: int, x: int) -> int:
    m = y if y >= x else x
    result = (m*m) - m + 1
    offset = abs(y - x)
    if (m == y and m % 2 == 1) or (m == x and m % 2 == 0):
        offset *= -1
    return result + offset


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        y, x = [int(s) for s in input().split(' ')]
        print(main(y, x))