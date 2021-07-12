from itertools import product
import sys
input = sys.stdin.readline

# 정수 a,b,c,d,e,f입력
a, b, c, d, e, f = map(int, input().split())

def solution():
  # -999~999 완전탐색
  for x in range(-999, 1000):
     for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            return

if __name__ == "__main__":
  solution()