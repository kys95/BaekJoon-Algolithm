import sys
input = sys.stdin.readline

# 보드크기 nxm
n, m = map(int, input().split())
# 로봇청소기 좌표(r,c), 바라보는 방향 direction
r, c, direction = map(int, input().split())
# 보드정보
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnleft():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

def solution(x, y, d):
    global result
    board[x][y] = 2  # 현재위치 청소
    result += 1
    turn = 0

    while True:
        turnleft()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if board[nx][ny] == 0:
            board[nx][ny] = 2  # 현재위치 청소
            result += 1
            x, y = nx, ny
            turn = 0
            continue

        else:
            turn += 1
        if turn == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if board[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
                turn = 0

if __name__ == "__main__":
    result = 0
    solution(r, c, direction)
    print(result)