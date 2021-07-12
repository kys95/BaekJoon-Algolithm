from itertools import combinations
import sys
input = sys.stdin.readline

# 카드 갯수 n, 최대합 m 입력
n, m = map(int, input().split())
# n개의 카드 입력
cards = list(map(int, input().split()))

def solution(m):
    # 세 장의 카드 합
    result = 0
    # n개의 카드 중 3개의 카드 뽑는 조합
    choices = combinations(cards, 3)
    for choice in choices:
        temp = sum(choice)
        if result < temp <= m:
            result = temp

    print(result)

if __name__ == "__main__":
    solution(m)