import sys
input = sys.stdin.readline

# 풍선갯수 n 입력
n = int(input().rstrip())
# 이동중인 화살 높이의 갯수 담을 dp
dp = [0] * (n + 1)
# 화살 높이 입력
arrows = list(map(int, input().split()))

def solution():
    # 화살 갯수
    count = 0
    # 화살 왼쪽부터 탐색
    for arrow in arrows:
        # 진행중인 화살높이가 아닐경우
        if dp[arrow] == 0:
            # 새로운 화살 추가
            count += 1
        else:
            # 전의 높이 갯수 갱신
            dp[arrow] -= 1
        # 이동중인 화살 높이 갯수 갱신
        dp[arrow - 1] += 1

    print(count)

if __name__ == '__main__':
    solution()