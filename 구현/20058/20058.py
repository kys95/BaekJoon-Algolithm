import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# 격자크기n, 파이어스톰 횟수 q
n, q = map(int, input().split())
n = 2 ** n
# 얼음
ice = [list(map(int, input().split())) for _ in range(n)]
# 파이어스톰 단계
arr = list(map(int, input().split()))

# 우,하,좌,상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시계방향으로 90도 회전
def rotate(K, ice):
    for x in range(0, n, K):
        for y in range(0, n, K):
            tmp = [ice[i][y:y + K] for i in range(x, x + K)]  # 격자 부분
            for i in range(K):
                for j in range(K):
                    ice[x + j][y + K - 1 - i] = tmp[i][j]

    # 주변 얼음의 양 check
    cnt = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and ice[nx][ny] > 0:
                    cnt[x][y] += 1
    # 얼음제거
    for x in range(n):
        for y in range(n):
            if ice[x][y] > 0 and cnt[x][y] < 3:
                ice[x][y] -= 1

def dfs(x, y):
    ice[x][y] = 0  # 방문처리
    tmp = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and ice[nx][ny] > 0:
            tmp += dfs(nx, ny)
    return tmp

if __name__ == "__main__":
    for L in arr:
        K = 2 ** L
        rotate(K, ice)  # 회전

    # 얼음의 합 출력
    print(sum(sum(i) for i in ice))

    # 가장 큰 덩어리
    ans = 0
    for x in range(n):
        for y in range(n):
            if ice[x][y] > 0:
                ans = max(ans, dfs(x, y))
    print(ans)