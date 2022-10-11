import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 공간의 크기 n 입력
n = int(input())
# 공간 상태
graph = [list(map(int, input().split())) for _ in range(n)]
# 아기상어 위치 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0
# 상,좌,우,하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y, size, time, eat):
    q = deque();
    canEat = []  # 이동경로, 먹을수 있는 물고기
    q.append((x, y))
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = time
    while q:
        length = len(q)
        while length:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0 or graph[nx][ny] == size:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
                        elif 0 < graph[nx][ny] < size:
                            heapq.heappush(canEat, (nx, ny))

            length -= 1

        if canEat:
            nx, ny = heapq.heappop(canEat)
            eat += 1
            if eat == size:  # 자기 크기만큼 먹은 경우
                eat = 0;
                size += 1
            graph[nx][ny] = 0
            return nx, ny, size, visited[x][y] + 1, eat

    print(time)
    sys.exit()


if __name__ == "__main__":
    size, time, eat = 2, 0, 0  # 크기, 시간, 먹은 횟수
    while True:
        x, y, size, time, eat = bfs(x, y, size, time, eat)