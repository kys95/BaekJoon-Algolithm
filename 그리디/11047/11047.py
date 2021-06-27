import sys

input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())
# 동전 리스트
coin = []
# 동전 입력
for _ in range(n):
    coin.append(int(input().rstrip()))

result = 0
for x in coin[::-1]:
    result += (k // x)
    k %= x

print(result)
