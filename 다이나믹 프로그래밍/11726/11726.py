import sys

sys.setrecursionlimit(10 ** 6)


def f(n):
    if cache[n]:
        return cache[n]

    cache[n] = n if n <= 2 else (f(n - 1) + f(n - 2)) % 10007

    return cache[n]


if __name__ == "__main__":
    n = int(input())
    cache = [0] * (n + 1)

    print(f(n))