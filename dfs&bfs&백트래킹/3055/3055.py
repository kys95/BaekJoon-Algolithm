import sys

input = sys.stdin.readline
from collections import deque

# R행 C열 입력
r, c = map(int, input().split())
# 그래프
graph = []
# 방문리스트
visited = [[False] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 그래프 정보 입력
for _ in range(r):
    graph.append(list(input().rstrip()))
# 물, 고슴도치 큐
water = deque()
animal = deque()
# 물, 고슴도치 좌표 확인
for i in range(r):
    for j in range(c):
        # 물이면
        if graph[i][j] == '*':
            water_start_x, water_start_y = i, j
            water.append([i, j])
        # 고슴도치면
        elif graph[i][j] == 'S':
            visited[i][j] = True
            animal_start_x, animal_start_y = i, j

# 최종이동횟수
count = 0


def move_water():
    length = len(water)
    while length:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계조건
            if 0 <= nx < r and 0 <= ny < c:
                # 빈칸일 때 물확장
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water.append([nx, ny])
        # 매분마다 고려하기 위함
        length -= 1


def move_animal(graph, x, y, visited):
    global count
    animal.append([x, y])
    while animal:
        length = len(animal)
        while length:
            x, y = animal.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 경계조건
                if 0 <= nx < r and 0 <= ny < c:
                    # 빈칸일 때
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        graph[nx][ny] = 'S'
                        visited[nx][ny] = True
                        animal.append([nx, ny])
                    # 비버굴 도착
                    elif graph[nx][ny] == 'D':
                        print(count + 1)
                        return
            length -= 1
        move_water()
        # 1분 싸이클
        count += 1
    print('KAKTUS')
    return


move_water()
move_animal(graph, animal_start_x, animal_start_y, visited)