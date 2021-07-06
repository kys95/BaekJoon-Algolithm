import sys
input = sys.stdin.readline
INF = 1e9

# 첫번째 전구 스위치 누름
def change(bulb):
    # 스위치 누르는 횟수
    count = 1
    bulb[0] = 1 - bulb[0]
    bulb[1] = 1 - bulb[1]

    for i in range(1, len(bulb)):
        if bulb[i - 1] != target[i - 1]:
            count += 1
            bulb[i - 1] = 1 - bulb[i - 1]
            bulb[i] = 1 - bulb[i]

            if i < len(bulb) - 1:
                bulb[i + 1] = 1 - bulb[i + 1]

    if bulb == target:
        return count
    return INF

# 첫번째 전구 스위치 안누름
def non_change(bulb):
    # 스위치 누르는 횟수
    count = 0
    for i in range(1, len(bulb)):
        if bulb[i - 1] != target[i - 1]:
            count += 1
            bulb[i - 1] = 1 - bulb[i - 1]
            bulb[i] = 1 - bulb[i]

            if i < len(bulb) - 1:
                bulb[i + 1] = 1 - bulb[i + 1]

    if bulb == target:
        return count
    return INF

if __name__ == '__main__':
    # 전구갯수 n 입력
    n = int(input().rstrip())
    # 전구1, 전구2 입력
    state = list(map(int, input().rstrip()))
    target = list(map(int, input().rstrip()))

    count_1 = change(state[:])
    count_2 = non_change(state[:])
    # 스위치 누르는 최솟값
    result = min(count_1, count_2)
    # 일치하지 않을 경우
    if result == INF:
        print(-1)
    else:
        print(result)