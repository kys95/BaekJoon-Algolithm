import sys

input = sys.stdin.readline
INF = int(1e9)
# 크레인 갯수 n 입력
n = int(input().rstrip())
# 각 크레인의 무게 제한 입력
cranes = list(map(int, input().split()))
# 박스 갯수 m 입력
m = int(input().rstrip())
# 각 박스 무게 입력
boxes = list(map(int, input().split()))


def solution():
    # 크레인 & 박스 내림차순 정렬
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    # 크레인 별 박스 옮기는 포지션
    pos = [0] * n

    # 어떠한 크레인도 하나의 박스를 옮길 수 없다면
    if cranes[0] < boxes[0]:
        print(-1)
        exit()
    else:
        # 이동 횟수
        count = 0
        # 옮기는 데 드는 최소 시간
        time = 0

        while count < m:

            for i in range(n):
                for j in range(pos[i], m):
                    if cranes[i] >= boxes[j]:
                        pos[i] += 1
                        count += 1
                        # 옮김 처리
                        boxes[j] = INF
                        break
                    else:
                        pos[i] += 1
            time += 1
    # 최소 시간 출력
    print(time)


if __name__ == '__main__':
    solution()