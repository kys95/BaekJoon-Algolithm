from collections import deque

if __name__ == "__main__":
  n, m, k = map(int, input().split())
  board = [[0 for _ in range(m)] for _ in range(n)]
  cases = []
  for _ in range(k):
    a, b = map(int, input().split())
    cases.append((a - 1, b - 1))
    board[a - 1][b - 1] = 1
  visited = [[0 for _ in range(m)] for _ in range(n)]
  #상,하,좌,우
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  ans = 0
  dq = deque()

  for a, b in cases:
    if visited[a][b] == 0:
      dq.append((a, b))
      visited[a][b] = 1

      cnt = 0
      while dq:

        x, y = dq.popleft()
        cnt += 1
        ans = max(ans, cnt)

        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
            dq.append((nx, ny))
            visited[nx][ny] = 1

  print(ans)