import sys
input = sys.stdin.readline

# 보드판 입력
board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
  print(-1)
else:
  print(board)
