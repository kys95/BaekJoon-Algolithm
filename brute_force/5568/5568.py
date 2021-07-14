from itertools import permutations
import sys
input = sys.stdin.readline

# 카드갯수 n 입력
n = int(input().rstrip())
# n개중 선택하는 갯수 k 입력
k = int(input().rstrip())
# n개의 카드 정보 입력할 리스트
cards = []
# n개의 카드 입력
for _ in range(n):
    cards.append(input().rstrip())  # 문자로 입력받음

def solution(k):
    # n개중 k개를 고르는 순열
    choices = permutations(cards, k)
    # 집합 자료형(중복 방지위함)
    result = set()
    for choice in choices:
        result.add(''.join(choice))  # 정수 만들기
    print(len(result))

if __name__ == "__main__":
    solution(k)