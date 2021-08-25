#!/usr/bin/env python3


from typing import Callable


def hailstone(n: int) -> int:
    return int(n/2) if n%2 == 0 else 3*n+1


def apply(input: int, rule: Callable) -> int:
    if input == 1:
        return 1
    return rule(input)


def main(input: str, collector: list = []) -> str:
    while True:
        collector.append(input)
        if input == '1':
            break
        input = str(apply(int(input), hailstone))
    return ' '.join(collector)


if __name__ == '__main__':
    print(main(input()))