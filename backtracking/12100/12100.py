# 1.보드판이 상하좌우로 5번 움직이는 경우의 수->각 경우에 따라 보드판의 상태가 달라짐(보드판 상태를 각 상태에 따라 유지시켜야함)
# 2.보드판이 상하좌우로 움직임에따라 블록의 움직임이 달라짐

import sys

input = sys.stdin.readline
from copy import deepcopy


# 블록을 위로 이동시킨 보드판을 반환
def moveUp(board):
    for j in range(n):
        idx = 0  # 비교대상이 되는 인덱스
        for i in range(1, n):  # 1행의 블록들은 위로 올라갈 수 없으므로
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0  # 이동하므로 0으로 갱신

                if board[idx][j] == 0:  # 위 블록이 0일경우
                    board[idx][j] = temp

                elif board[idx][j] == temp:  # 위 블록과 같을 경우
                    board[idx][j] = temp * 2
                    idx += 1

                else:  # 위 블록과 다를 경우
                    idx += 1
                    board[idx][j] = temp  # 현재 블록을 유지하고 인덱스를 +1

    return board


# 블록을 아래로 이동시킨 보드판을 반환
def moveDown(board):
    for j in range(n):
        idx = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0

                if board[idx][j] == 0:
                    board[idx][j] = temp

                elif board[idx][j] == temp:
                    board[idx][j] = temp * 2
                    idx -= 1

                else:
                    idx -= 1
                    board[idx][j] = temp

    return board


# 블록을 오른쪽으로 이동시킨 보드판을 반환
def moveRight(board):
    for i in range(n):
        idx = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][idx] == 0:
                    board[i][idx] = temp

                elif board[i][idx] == temp:
                    board[i][idx] = temp * 2
                    idx -= 1

                else:
                    idx -= 1
                    board[i][idx] = temp

    return board


# 블록을 왼쪽으로 이동시킨 보드판을 반환
def moveLeft(board):
    for i in range(n):
        idx = 0
        for j in range(1, n):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][idx] == 0:
                    board[i][idx] = temp

                elif board[i][idx] == temp:
                    board[i][idx] = temp * 2
                    idx += 1

                else:
                    idx += 1
                    board[i][idx] = temp

    return board


def dfs(board, cnt):
    global result

    if cnt == 5:  # 보드판이 5번움직인 경우
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return

    dfs(moveUp(deepcopy(board)), cnt + 1)  # 상
    dfs(moveDown(deepcopy(board)), cnt + 1)  # 하
    dfs(moveRight(deepcopy(board)), cnt + 1)  # 우
    dfs(moveLeft(deepcopy(board)), cnt + 1)  # 좌


if __name__ == "__main__":
    n = int(input())  # 보드의 크기
    board = [list(map(int, input().split())) for _ in range(n)]

    result = 0  # 가장 큰 블록
    dfs(board, 0)
    print(result)