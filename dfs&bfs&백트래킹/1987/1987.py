from collections import deque

if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    visited = [[set() for _ in range(c)] for _ in range(r)]
    # 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0].add(board[0][0])
    dq = deque()
    dq.append((0, 0, board[0][0], 1))
    ans = 1

    while dq:
        x, y, alpha, cnt = dq.popleft()  # alpha: ex)abc..
        ans = max(ans, cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alpha:
                new_alpha = alpha + board[nx][ny]
                if new_alpha not in visited[nx][ny]:
                    visited[nx][ny].add(new_alpha)
                    dq.append((nx, ny, new_alpha, cnt + 1))

    print(ans)