from collections import deque
import sys
input = sys.stdin.readline

# 격자크기 N, 명령갯수 M
N, M = map(int, input().split())
# 격자
graph = [list(map(int, input().split())) for _ in range(N)]
# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 명령
orders = []
for _ in range(M):
    d, s = map(int, input().split())  # 방향, 거리
    orders.append((d, s))
# 초기 구름 위치
cloud = deque()
cloud.append((N - 1, 0))
cloud.append((N - 1, 1))
cloud.append((N - 2, 0))
cloud.append((N - 2, 1))

def solution():
    for d, s in orders:
        temp = []  # 이동할 구름 좌표 담을 리스트
        for _ in range(len(cloud)):
            x, y = cloud.popleft()
            nx = (s * dx[d - 1] + x) % N
            ny = (s * dy[d - 1] + y) % N
            graph[nx][ny] += 1  # 구름이 있는 칸에 비가 1씩 내림
            temp.append((nx, ny))

        for x, y in temp:
            cnt = 0  # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수
            for idx in range(4):
                nx = x + dx[idx * 2 + 1]
                ny = y + dy[idx * 2 + 1]
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1:
                    cnt += 1
            graph[x][y] += cnt  # 구름이 있는 칸에 비가 1씩 내림

        for i in range(N):
            for j in range(N):
                if graph[i][j] >= 2 and (i, j) not in temp:  # 물의양이 2이상 & 3에서 구름이 사라진 칸이아님
                    cloud.append((i, j))  # 구름 생김
                    graph[i][j] -= 2  # 구름이 생기면 물의 양이 2만큼 줄어듦
    result = 0
    for i in range(N):
        for j in range(N):
            result += graph[i][j]
    print(result)

if __name__ == "__main__":
    solution()
