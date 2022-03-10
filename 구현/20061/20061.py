# 1.초록색보드, 파란색보드 따로 구현
# 2.초록색보드,파란색보드에 블록 놓음
# 3.초록색보드(행),파란색보드(열)이 블록으로 가득찬 경우 확인
# 4.가득차면 블록제거
# 5.연한보드에 블록 남아있는지 확인
# 6.남아있으면 블록제거

import sys
input = sys.stdin.readline

def drop_green(t, y):
    x = 0
    if t == 1 or t == 3:
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1
        # 실제 정착되는 행 위치
        x -= 1
        green[x][y] = 1
        if t == 3:
            green[x - 1][y] = 1
    else:
        for i in range(6):
            if green[i][y] == 1 or green[i][y + 1] == 1:
                break
            x += 1
        x -= 1
        green[x][y] = 1
        green[x][y + 1] = 1

def drop_blue(t, x):
    y = 0
    if t == 1 or t == 2:
        for j in range(6):
            if blue[x][j] == 1:
                break
            y += 1
        y -= 1
        blue[x][y] = 1
        if t == 2:
            blue[x][y - 1] = 1
    else:
        for j in range(6):
            if blue[x][j] == 1 or blue[x + 1][j] == 1:
                break
            y += 1
        y -= 1
        blue[x][y] = 1
        blue[x + 1][y] = 1

# 2~4번 행중 가득찬 여부 확인
# 가득찬 행이 있는지 확인하고 있으면 한줄을 없애고 위에 있는 줄들을 내려오게 한다.
# 문제 내용상 연한 색깔영역 0,1행에서는 블록이 한 줄 가득차는 경우가 없으므로 2~5행 번호만 확인한다.
def check():
    global answer
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                cnt += 1
        # 한줄이 가득찬 경우 점수 득점, 해당 행을 없애고 위에 있는 줄이 한줄 내려온다.
        if cnt == 4:
            # print(cnt)
            # print(green)
            # print('after{}'.format(i))
            remove('green', i)
            answer += 1

    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if blue[i][j] == 1:
                cnt += 1
        if cnt == 4:
            remove('blue', j)
            answer += 1

# 기본적으로 위에 있는 행들을 그대로 들고오되, 0번째 행은 블록을 비워주도록 구현
def remove(color, index):
    if color == 'green':
        for i in range(index, -1, -1):
            if i == 0:
                for j in range(4):
                    green[i][j] = 0
                return
            for j in range(4):
                green[i][j] = green[i - 1][j]
    else:
        for j in range(index, -1, -1):
            if j == 0:
                for i in range(4):
                    blue[i][j] = 0
                return
            for i in range(4):
                blue[i][j] = blue[i][j - 1]


# 연한 색깔 영역에 블록이 남아있는지 확인
# 해당 영역에 블록이 존재하면 제일 아래행을 삭제하고 한행씩 내려온다.
def check_light_area():
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                remove('green', 5)
                break
    for j in range(2):
        for i in range(4):
            if blue[i][j] == 1:
                remove('blue', 5)
                break

if __name__ == "__main__":
    green = [[0 for _ in range(4)] for _ in range(6)]
    blue = [[0 for _ in range(6)] for _ in range(4)]
    answer = 0

    n = int(input())  # 블록놓은 횟수
    for _ in range(n):
        t, x, y = map(int, input().split())

        drop_green(t, y)  # 초록색보드에 블록놓음
        drop_blue(t, x)  # 파란색보드에 블록놓음

        check()
        check_light_area()

blockcnt = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j] == 1:
            blockcnt += 1

for i in range(4):
    for j in range(2, 6):
        if blue[i][j] == 1:
            blockcnt += 1

print(answer)
print(blockcnt)