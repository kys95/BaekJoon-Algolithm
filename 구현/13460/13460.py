import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = set()
q = deque()                 # 빨간,파란 구슬 담을 큐
dx = [1,-1,0,0]             # 방향
dy = [0, 0, 1, -1]

rx, ry, bx, by = 0, 0, 0, 0   # 빨간색 구슬 좌표, 파란색 구슬 좌표
for i in range(n):
  for j in range(m):
    if board[i][j] == 'R':
      rx, ry = i, j
    elif board[i][j] == 'B':
      bx, by = i, j
q.append((rx,ry,bx,by,0))
visited.add((rx,ry,bx,by))        # 방문 체크

# 구슬 이동
def move(x,y,dx,dy):
  result = 0
  # 다음위치가 벽이 아니고, 현재위치가 구멍이 아닐때 까지
  while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    result += 1
  return x,y,result

def solution():
  while q:
    rx, ry, bx, by, cnt = q.popleft()
   
    if cnt >= 10:
      break
    for i in range(4):
      nrx, nry, rcnt = move(rx,ry,dx[i],dy[i])
      nbx, nby, bcnt = move(bx,by,dx[i],dy[i])

      if board[nbx][nby] != 'O':          # 성공조건
        if board[nrx][nry] == 'O':       
          print(cnt+1)
          return
        if nrx == nbx and nry == nby:     # 빨간,파란 구슬 위치가 같을 때
          if rcnt > bcnt:                 # 많이 이동한 구슬이 한 칸 뒤로
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        if not (nrx,nry,nbx,nby) in visited:    # 방문 여부 확인
          
          q.append((nrx,nry,nbx,nby,cnt+1))
          visited.add((nrx,nry,nbx,nby))

  print(-1)
  
if __name__ == "__main__":
  solution()