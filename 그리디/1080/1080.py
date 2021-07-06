import sys
input = sys.stdin.readline

# 행렬 A&B 최종 비교
def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True

# 3*3 뒤집기
def convert(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]

if __name__ == '__main__':
    # 행렬의 크기 n, m 입력
    n, m = map(int, input().split())
    # 행렬A, 행렬B 입력
    A = [list(map(int, input().rstrip())) for _ in range(n)]
    B = [list(map(int, input().rstrip())) for _ in range(n)]
    # 뒤집는 횟수
    count = 0
    # 행렬 A와 B 비교 (x : 0~n-2, y : 0~m-2)
    for i in range(0, n - 2):
        for j in range(0, m - 2):
            # 일치하지 않을 경우 3 * 3 부분행렬 뒤집기
            if A[i][j] != B[i][j]:
                count += 1
                convert(i, j)
    # 행렬 A와 B 최종 비교
    if check():
        print(count)
    else:
        print(-1)