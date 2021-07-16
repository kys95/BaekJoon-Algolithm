from itertools import combinations
import sys
input = sys.stdin.readline

# 모눈종이 크기 h,w입력
h, w = map(int, input().split())
# 스티커갯수 n 입력
n = int(input().rstrip())
# 스티커 크기 담을 리스트
stickers = []
# 스티커 크기 입력
for _ in range(n):
    x, y = map(int, input().split())
    stickers.append((x, y))

def solution(h, w):
    # n개의 스티커중 2개 선택하는 조합
    choices = combinations(stickers, 2)
    # 스티커 최대 넓이
    result = 0
    for choice in choices:
        a, b = choice  # 스티커 2개
        # 스티커 2개 넓이
        temp = a[0] * a[1] + b[0] * b[1]
        if a[0] + b[0] <= h and max(a[1], b[1]) <= w:
            result = max(result, temp)
        elif a[0] + b[0] <= w and max(a[1], b[1]) <= h:
            result = max(result, temp)
        elif a[0] + b[1] <= h and max(a[1], b[0]) <= w:
            result = max(result, temp)
        elif a[0] + b[1] <= w and max(a[1], b[0]) <= h:
            result = max(result, temp)
        elif a[1] + b[0] <= h and max(a[0], b[1]) <= w:
            result = max(result, temp)
        elif a[1] + b[0] <= w and max(a[0], b[1]) <= h:
            result = max(result, temp)
        elif a[1] + b[1] <= h and max(a[0], b[0]) <= w:
            result = max(result, temp)
        elif a[1] + b[1] <= w and max(a[0], b[0]) <= h:
            result = max(result, temp)

    print(result)

if __name__ == "__main__":
    solution(h, w)