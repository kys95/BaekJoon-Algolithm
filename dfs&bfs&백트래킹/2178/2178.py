from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    # 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((0, 0))  # (0,0) start
    board[0][0] = int(board[0][0])
    visited[0][0] = 1

    while dq:
        x, y = dq.popleft()

        if x == n - 1 and y == m - 1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] != '0':
                board[nx][ny] = board[x][y] + 1
                dq.append((nx, ny))
                visited[nx][ny] = 1

    print(board[n - 1][m - 1])