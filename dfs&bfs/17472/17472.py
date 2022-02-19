import sys

input = sys.stdin.readline
from collections import deque


def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]


def makeBridge():  # 다리만들기

    for (x, y), curIsland in island.items():  # 섬의 좌표와 번호

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dist = 0  # 다리길이

            while True:

                if 0 <= nx < n and 0 <= ny < m:

                    toIsland = island.get((nx, ny))  # 다른섬

                    if curIsland == toIsland:  # 같은 섬
                        break

                    elif toIsland == None:  # 바다
                        nx += dx[i]
                        ny += dy[i]
                        dist += 1
                        continue

                    else:  # 다른 섬
                        if dist < 2:
                            break
                        else:
                            bridgeList.append((dist, curIsland, toIsland))

                            break

                else:
                    break
    return


def bfs(x, y, num):  # 섬의 번호 정하기

    q = deque()
    q.append((x, y))
    island[(x, y)] = num

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    island[(nx, ny)] = num

    return


if __name__ == "__main__":
    n, m = map(int, input().split())  # nxm 지도크기
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문리스트
    island = dict()  # 섬 key:좌표, value:번호
    num = 0  # 섬 번호

    # 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                num += 1
                visited[i][j] = True
                bfs(i, j, num)

    bridgeList = []

    makeBridge()

    parent = [0] * (num + 1)
    for i in range(num + 1):
        parent[i] = i

    bridgeList.sort()
    line = 0
    result = 0
    for bridge in bridgeList:
        dist, curIsland, toIsland = bridge
        if findParent(curIsland) != findParent(toIsland):
            unionParent(curIsland, toIsland)
            result += dist
            line += 1

    if line == num - 1:
        print(result)
    else:
        print(-1)