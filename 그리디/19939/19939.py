import sys

input = sys.stdin.readline

# 공의 갯수 n, 바구니의 갯수 k 입력
n, k = map(int, input().split())


def solution(n, k):
    # 조건에 만족하지 못할 경우
    if n < k * (k + 1) // 2:
        return -1
    else:
        # 나머지
        left = n - k * (k + 1) // 2
        if left % k == 0:
            return k - 1
        else:
            return k


if __name__ == '__main__':
    print(solution(n, k))