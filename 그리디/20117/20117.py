import sys
input = sys.stdin.readline

# 호반우 갯수 n 입력
n = int(input().rstrip())
# 호반우 가격 입력
prices = list(map(int, input().split()))

def solution(n):
    # 호반우 가격 오름차순 정렬
    prices.sort()
    # 품질계산법에 따른 최종 가격
    price = 0
    # 묶음 = 가장 값싼 것 & 가장 비싼 것
    for i in range(n // 2):
        price += prices[n - 1 - i] * 2
    # 묶음 처리 안된것이 있는경우
    if n % 2:
        price += prices[n // 2]

    print(price)

if __name__ == '__main__':
    solution(n)