import sys

input = sys.stdin.readline
from itertools import combinations
from collections import deque

INF = int(1e9)


def bfs(case):
    node_cnt = 0  # 하나의 선거구 안의 구역갯수
    sum_cnt = 0  # 하나의 선거구의 총 인구수

    start = case[0]  # 케이스 중 첫번째 구역
    visited = [False] * (n + 1)  # 방문리스트

    q = deque()
    q.append(start)
    visited[start] = True

    node_cnt += 1
    sum_cnt += people[start]

    while q:

        node = q.popleft()

        # 인접한 구역중 케이스에 속하고 방문하지 않은 구역 찾기
        for v in graph[node]:
            if v in case and visited[v] == False:
                q.append(v)
                visited[v] = True
                node_cnt += 1
                sum_cnt += people[v]

    return sum_cnt, node_cnt


if __name__ == "__main__":

    n = int(input())  # 구역의 갯수
    people = [0]  # 인덱스1부터 시작하기 위함
    people += list(map(int, input().split()))  # 인구수 입력

    result = INF

    # 인접한 구역의 번호 입력
    graph = [[]]
    for _ in range(n):
        data = list(map(int, input().split()))
        if data[0] != 0:
            graph.append(data[1:])
        else:
            graph.append([0])

    for i in range(1, n // 2 + 1):
        cases = list(combinations([x for x in range(1, n + 1)], i))

        for case in cases:

            sum1, num_of_node1 = bfs(case)
            sum2, num_of_node2 = bfs([x for x in range(1, n + 1) if x not in case])

            # 두선거구로 나눌 수 있는 경우
            if num_of_node1 + num_of_node2 == n:
                result = min(result, abs(sum1 - sum2))

    if result != INF:
        print(result)
    else:
        print(-1)