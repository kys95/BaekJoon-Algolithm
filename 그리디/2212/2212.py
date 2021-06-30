import sys

input = sys.stdin.readline

# 센서의 갯수 n 입력
n = int(input().rstrip())
# 집중국의 갯수 k 입력
k = int(input().rstrip())
# n개의 센서 입력
sensors = list(map(int, input().split()))


def solution():
    global n, k
    # 수신 가능 영역 0일 경우
    if n <= k:
        print(0)
    else:
        # 센서 오름차순 정렬
        sensors.sort()
        # 인접한 두 센서의 거리차를 담을 리스트
        dis = []
        # 인접한 두 센서 거리 계산
        for i in range(1, n):
            dis.append(sensors[i] - sensors[i - 1])
        # dis 리스트 내림차순 정렬
        dis.sort(reverse=True)
        # k개의 영역을 나눈 후 수신 가능 영역 출력
        print(sum(dis[k - 1:]))


if __name__ == '__main__':
    solution()