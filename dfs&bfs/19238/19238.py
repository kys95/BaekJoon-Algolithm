from collections import deque
import heapq
import sys
input = sys.stdin.readline

# n,m,fuel
n, m, fuel = map(int, input().split())
# graph
graph = [list(map(int, input().split())) for _ in range(n)]
# 택시기사 위치
x, y = map(int, input().split())
x -= 1
y -= 1
# 승객
customers = {}
for _ in range(m):
    a, b, c, d = map(int, input().split())
    customers[(a - 1, b - 1)] = (c - 1, d - 1)
# 상,좌,우,하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs1(x, y, customers, graph):
    flag = True
    q = deque()
    heap = []
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    if (x, y) in customers:
        return x, y, 0, flag

    while q:
        qlen = len(q)
        while qlen:
            x, y, cnt = q.popleft()
            qlen -= 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = True
                        if (nx, ny) in customers:
                            heapq.heappush(heap, (nx, ny, cnt + 1))

        if heap:
            x, y, cnt = heapq.heappop(heap)
            return x, y, cnt, flag

    flag = False
    return x, y, cnt, flag

def bfs2(x, y, customers, graph):
    flag = True
    q = deque()
    xdes, ydes = customers[(x, y)]

    q.append((x, y, 0))
    del customers[(x, y)]
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while q:
        x, y, cnt = q.popleft()
        if x == xdes and y == ydes:
            return x, y, cnt, flag
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
    flag = False
    return x, y, cnt, flag

if __name__ == "__main__":
    for _ in range(m):
        if fuel < 0:
            print(-1)
            sys.exit()
        # 손님 출발지 찾기
        x, y, dis, flag = bfs1(x, y, customers, graph)
        if flag == False:
            print(-1)
            sys.exit()
        # 택시 -> 손님 출발지까지 가는데 연료 소모
        fuel -= dis
        if fuel < 0:
            print(-1)
            sys.exit()

        # 손님 도착지 찾기
        x, y, dis, flag = bfs2(x, y, customers, graph)
        if flag == False:
            print(-1)
            sys.exit()
        # 출발지 -> 도착지까지 가는데 연료 소모
        fuel -= dis
        if fuel < 0:
            print(-1)
            sys.exit()
        # 소모한 연료 양의 두 배가 충전
        fuel += dis * 2

    print(fuel)