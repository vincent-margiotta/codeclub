#!/usr/bin/env python3


def main(n: int, string_numbers: str) -> str:
    nth_triangular = n*(n+1)//2  # AKA the sum of the integers up to n
    integer_list = [int(s) for s in string_numbers.split(' ')]
    return nth_triangular-sum(integer_list)


if __name__ == '__main__':
    n = int(input())
    string_numbers = input()
    print(main(n, string_numbers))