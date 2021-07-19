import sys
input = sys.stdin.readline

# 검은 바둑알(1)위치 담을 리스트 흰 바둑알(0)위치 담을 리스트
black = []
white = []
# 19x19바둑판 입력
for i in range(19):
    data = list(map(int, input().split()))
    for j in range(19):
        if data[j] == 1:
            black.append((i, j))
        elif data[j] == 2:
            white.append((i, j))

def solution(arr):
    # 4가지 방향확인(오른쪽, 오른쪽 대각선 아래, 오른쪽 대각선 위, 아래)
    for x, y in arr:  # 오른쪽
        count = 1
        for i in range(1, 5):
            if (x, y + i) in arr:
                count += 1
            else:
                break

            if count == 5:
                # 6개이상이 놓여있는지 확인
                if (x, y - 1) not in arr and (x, y + 5) not in arr:
                    return [True, x + 1, y + 1]

    for x, y in arr:  # 오른쪽 대각선 아래
        count = 1
        for i in range(1, 5):
            if (x + i, y + i) in arr:
                count += 1
            else:
                break

            if count == 5:
                # 6개이상이 놓여있는지 확인
                if (x - 1, y - 1) not in arr and (x + 5, y + 5) not in arr:
                    return [True, x + 1, y + 1]

    for x, y in arr:  # 오른쪽 대각선 위
        count = 1
        for i in range(1, 5):
            if (x - i, y + i) in arr:
                count += 1
            else:
                break

            if count == 5:
                # 6개이상이 놓여있는지 확인
                if (x + 1, y - 1) not in arr and (x - 5, y + 5) not in arr:
                    return [True, x + 1, y + 1]

    for x, y in arr:  # 아래
        count = 1
        for i in range(1, 5):
            if (x + i, y) in arr:
                count += 1
            else:
                break

            if count == 5:
                # 6개이상이 놓여있는지 확인
                if (x - 1, y) not in arr and (x + 5, y) not in arr:
                    return [True, x + 1, y + 1]

    return [False]

if __name__ == "__main__":
    result = solution(black)
    if result[0]:
        print(1)
        print(result[1], result[2])
    else:
        result = solution(white)
        if result[0]:
            print(2)
            print(result[1], result[2])
        else:
            print(0)