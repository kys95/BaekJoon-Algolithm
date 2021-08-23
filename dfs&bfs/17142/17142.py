from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline
INF = int(1e9)

# 연구소크기 n, 바이러스 갯수m 입력
n, m = map(int, input().split())
# 연구소 상태
graph = [list(map(int, input().split())) for _ in range(n)]
# 바이러스 위치
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j, 0))  # x좌표,y좌표,시간
# 상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(fake):
    for i in range(n):
        for j in range(n):
            if fake[i][j] == 0:
                return False
    return True

def bfs(choice, graph):
    q = deque()
    fake = deepcopy(graph)
    q.extend(choice)
    visited = [[False] * n for _ in range(n)]
    time = 0  # 시간
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and fake[nx][ny] != 1:
                visited[nx][ny] = True
                if fake[nx][ny] == 0:
                    time = cnt + 1
                    fake[nx][ny] = 2
                q.append((nx, ny, cnt + 1))

    # 모든 바이러스 퍼뜨렸는 지 확인
    if check(fake):
        return time
    else:
        return -1

if __name__ == "__main__":
    # 바이러스 m개 조합
    choices = list(combinations(virus, m))
    result = INF
    for choice in choices:
        temp = bfs(choice, graph)

        if result > temp and temp != -1:
            result = temp

    if result != INF:
        print(result)
    else:
        print(-1)