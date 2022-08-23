from collections import deque


def bfs(start, goal):
    check = [False] * n
    dq = deque()
    check[start] = True
    dq.append((start, 0))

    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d

        for next in range(n):
            if connect[now][next] and not check[next]:
                check[next] = True
                dq.append((next, d + 1))


if __name__ == "__main__":
    n, m = map(int, input().split())
    connect = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        connect[a - 1][b - 1] = connect[b - 1][a - 1] = True

    dist = [[0 for _ in range(n)] for _ in range(n)]

    INF = int(1e9)
    answer = -1
    answer_total = INF

    for i in range(n):
        total = 0
        for j in range(n):
            if i != j:
                if dist[i][j] == 0:
                    dist[i][j] = dist[j][i] = bfs(i, j)

                total += dist[i][j]

        if answer_total > total:
            answer = i
            answer_total = total

    print(answer + 1)