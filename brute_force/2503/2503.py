from itertools import permutations
import sys
input = sys.stdin.readline

# 질문갯수 n 입력
n = int(input().rstrip())
# 질문 담을 리스트
ask = []
# 정수, 스트라이크, 볼 입력
for _ in range(n):
    num, strike, ball = map(str, input().split())
    strike = int(strike)
    ball = int(ball)
    ask.append((num, strike, ball))

def check(choice, ask):
    s, b = 0, 0  # 스트라이크, 볼 판정

    for i in range(3):
        for j in range(3):
            if choice[i] == int(ask[0][j]):
                if i == j:
                    s += 1
                else:
                    b += 1

    if s == ask[1] and b == ask[2]:
        return True
    else:
        return False

def solution(n):
    # 1~9까지 3뽑는 순열
    choices = permutations(list(range(1, 10)), 3)

    # 최종 갯수
    result = 0
    # 조합마다 질문한 정수와 비교
    for choice in choices:
        temp = 0
        for i in range(n):

            if check(choice, ask[i]):
                temp += 1
                if temp == n:
                    result += 1
            else:
                break

    print(result)

if __name__ == "__main__":
    solution(n)