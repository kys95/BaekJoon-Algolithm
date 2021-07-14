import math
import sys
input = sys.stdin.readline

# 정수 n 입력
n = int(input().rstrip())

def solution(n):
    # dp 생성
    dp = [0] * (n + 1)
    # 제곱수 합
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(i ** 2, (i + 1) ** 2):
            if j == n + 1:
                break
            if j == i ** 2:
                dp[j] = 1

                continue
            arr = []
            for k in range(1 ** 2, int(math.sqrt(j)) + 1):
                arr.append(dp[k ** 2] + dp[j - k ** 2])

            dp[j] = min(arr)

    print(dp[n])

if __name__ == "__main__":
    solution(n)