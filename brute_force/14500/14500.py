import sys
input = sys.stdin.readline

# nxm크기
n, m = map(int, input().split())
# 그래프(종이)
graph = []
# 종이에 쓰인 숫자
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 테트로미노 19가지 모양
board = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

def solution(x, y):
    global result
    for i in range(19):  # 19가지 테트로미노 모양
        temp = 0  # 각 테트로미노가 놓인 칸의 수의 합
        flag = True  # 테트로미노 성공
        for j in range(4):  # 4칸
            nx = x + board[i][j][0]
            ny = y + board[i][j][1]

            if 0 <= nx < n and 0 <= ny < m:
                temp += graph[nx][ny]
            else:
                flag = False  # 테트로미노 만들기 실패

        if flag:
            result = max(result, temp)

if __name__ == "__main__":
    result = 0
    for i in range(n):
        for j in range(m):
            solution(i, j)
    print(result)