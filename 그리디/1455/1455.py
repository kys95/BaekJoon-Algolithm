import sys
input = sys.stdin.readline

# 뒤집기
def flip(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            coins[i][j] = 1 - coins[i][j]


def solution(x, y):
    # 뒤집는 횟수
    count = 0
    # 오른쪽 밑에서 부터 확인
    for i in range(x - 1, -1, -1):
        for j in range(y - 1, -1, -1):
            if coins[i][j] == 1:
                count += 1
                flip(i, j)
    print(count)


if __name__ == '__main__':
    # 세로크기 n, 가로크기 m 입력
    n, m = map(int, input().split())
    # 동전상태 담을 리스트
    coins = []
    # 동전상태 입력
    for _ in range(n):
        coins.append(list(map(int, input().rstrip())))

    solution(n, m)