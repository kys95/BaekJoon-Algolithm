# 다익스트라
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    INF = int(1e9)
    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(start)

    cnt = 0
    max_dist = 0
    for d in distance:
        if d != INF:
            cnt += 1
            max_dist = max(max_dist, d)

    print(cnt - 1, max_dist)