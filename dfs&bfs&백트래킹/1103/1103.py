import sys

input = sys.stdin.readline
# 가로N, 세로M
N, M = map(int, input().split())
# 보드
board = []
for _ in range(N):
    board.append(input().rstrip())
# dp 초기화
dp = [[0] * M for _ in range(N)]
# 방문리스트
visited = [[False] * M for _ in range(N)]
# 상,하,좌,우 이동거리
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최종이동횟수
result = 0


def dfs(x, y, count):
    global result
    result = max(result, count)
    # 상,하,좌,우 확인
    for i in range(4):
        nx = x + dx[i] * int(board[x][y])
        ny = y + dy[i] * int(board[x][y])
        # 경계확인, H확인, 이동횟수확인
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H' and count + 1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = count + 1
                visited[nx][ny] = True
                dfs(nx, ny, count + 1)
                visited[nx][ny] = False


dfs(0, 0, 0)
print(result + 1)