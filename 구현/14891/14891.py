from collections import deque
import sys
input = sys.stdin.readline

# 4개톱니바퀴
gear = {}
for i in range(1, 5):
    gear[i] = deque(list(map(int, list(input().rstrip()))))  # 톱니바퀴1,2,3,4번
# 회전횟수 k
k = int(input().rstrip())
# 회전시킬 톱니바퀴 번호, 방향
data = []
for _ in range(k):
    idx, d = map(int, input().split())
    data.append((idx, d))
# 오른쪽 확인
def checkRight(start, direction):
    # 톱니바퀴 번호 넘어감 or 맞닿은 극이 같을 경우 무시
    if start > 4 or gear[start - 1][2] == gear[start][6]:
        return

    # 오른쪽 확인
    if gear[start - 1][2] != gear[start][6]:
        # 오른쪽 톱니바퀴 먼저 확인
        checkRight(start + 1, -direction)
        # 회전
        gear[start].rotate(direction)
# 왼쪽확인
def checkLeft(start, direction):
    # 톱니바퀴 번호 넘어감 or 맞닿은 극이 같을 경우 무시
    if start < 1 or gear[start + 1][6] == gear[start][2]:
        return

        # 왼쪽 확인
    if gear[start + 1][6] != gear[start][2]:
        # 왼쪽 톱니바퀴 먼저 확인
        checkLeft(start - 1, -direction)
        # 회전
        gear[start].rotate(direction)

def solution(gear, data):
    for idx, d in data:
        checkRight(idx + 1, -d)
        checkLeft(idx - 1, -d)

        # 회전
        gear[idx].rotate(d)

    # 12시방향 확인
    result = 0
    for i in range(1, 5):
        if gear[i][0] == 1:  # S극
            result += (2 ** (i - 1))

    return result


if __name__ == "__main__":
    score = solution(gear, data)
    print(score)