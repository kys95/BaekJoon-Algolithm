from collections import deque
import sys

input = sys.stdin.readline

# 컨베이어벨트 갯수n, 내구도0인 칸의 갯수 k 입력
n, k = map(int, input().split())
# 컨베이어벨트 내구도 입력
arr = deque(map(int, input().split()))
# 로봇
robot = deque([0] * n)


def solution():
    result = 1
    while True:
        # 1단계
        arr.rotate(1)
        robot.rotate(1)
        robot[n - 1] = 0  # 내려가는 위치에 로봇 삭제

        # 2단계
        for i in range(n - 2, -1, -1):
            if robot[i] != 0 and robot[i + 1] == 0 and arr[i + 1] >= 1:
                arr[i + 1] -= 1  # 내구도 감소
                robot[i + 1] = robot[i]  # 로봇 이동
                robot[i] = 0
        robot[n - 1] = 0

        # 3단계
        if arr[0] > 0 and robot[0] == 0:
            arr[0] -= 1
            robot[0] = 1

        # 4단계
        count = 0
        for belt in arr:
            if belt == 0:
                count += 1
        # 내구도가 0인 칸의 개수가 K개 이상이라면 종료
        if count >= k:
            return result

        result += 1


if __name__ == "__main__":
    print(solution())