from collections import deque
import sys
input = sys.stdin.readline
# 보드의 크기 n
n = int(input().rstrip())
# 보드 초기화
board = [[0] * (n + 1) for _ in range(n + 1)]
# 사과갯수 k
k = int(input().rstrip())
# 사과 위치
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 'apple'  # 사과 위치 설정
# 뱀의 방향변환 횟수 L
L = int(input().rstrip())
# 뱀의 뱡향
directions = []
for _ in range(L):
    t, d = map(str, input().split())
    directions.append((int(t), d))
# 동,남,서,북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def FindDirection(direc, d):
    if d == 'D':
        direc = (direc + 1) % 4
    else:
        direc = (direc - 1) % 4
    return direc

def solution():
    idx = 0
    x, y = 1, 1
    board[x][y] = 1  # 뱀의 위치
    snake = deque()
    snake.append((x, y))
    direc = 0  # 초기방향(동쪽)
    count = 0  # 게임시간

    while True:
        if idx < L and count == directions[idx][0]:  # 뱀의 방향변환 시간 일치
            direc = FindDirection(direc, directions[idx][1])
            idx += 1

        nx = x + dx[direc]
        ny = y + dy[direc]
        # 보드 벗어나지않고 뱀 몸통 부딪히지 않는 경우
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 1:
            # 사과 못먹는 경우
            if board[nx][ny] != 'apple':
                tx, ty = snake.popleft()  # 꼬리 삭제
                board[tx][ty] = 0
            snake.append((nx, ny))
            x, y = nx, ny  # 뱀의 머리
            board[nx][ny] = 1  # 뱀의 위치
            count += 1  # 시간 설정

        else:
            count += 1
            break
    return count

if __name__ == "__main__":
    result = solution()
    print(result)