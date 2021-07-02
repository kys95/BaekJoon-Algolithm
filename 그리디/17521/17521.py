import sys

input = sys.stdin.readline

# 요일 수 n, 초기 현금 w 입력
n, w = map(int, input().split())
# 코인 가격담을 리스트
prices = []
for _ in range(n):
    prices.append(int(input().rstrip()))


def solution(w):
    # 매수가, 매도가
    buy, sell = 0, 0
    for i in range(1, len(prices)):
        # 상방
        if prices[i - 1] < prices[i]:
            # 매수가가 정해지지 않은 경우
            if buy == 0:
                buy = prices[i - 1]
            sell = prices[i]
        # 하방
        elif prices[i - 1] > prices[i]:
            # 매수가 매도가가 정해진 경우만
            if buy != 0 and sell != 0:
                profit = (sell - buy) * (w // buy)
                w += profit
                # 매수가, 매도가 0으로 초기화
                buy, sell = 0, 0
    # 매수가, 매도가 남아있을 경우
    if buy != 0 and sell != 0:
        profit = (sell - buy) * (w // buy)
        w += profit
    print(w)


if __name__ == '__main__':
    solution(w)
