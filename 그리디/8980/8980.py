import sys

input = sys.stdin.readline

# 마을수 n, 트럭용량 c 입력
n, c = map(int, input().split())
# 박스의 갯수 m 입력
m = int(input().rstrip())
# 박스 정보 담을 리스트
boxes = []
# m개의 박스 정보 입력
for _ in range(m):
    # 보내는 마을번호, 받는 마을번호, 보내는 박스 갯수
    a, b, k = map(int, input().split())
    boxes.append((a, b, k))


def solution(n, c):
    # 받는 마을번호가 작은것부터 큰 순서대로 오름차순 정렬
    boxes.sort(key=lambda x: x[1])
    # 마을 당 보낼 수 있는 용량 리스트
    delivery = [c] * (n + 1)
    # 최대 박스 수
    result = 0

    # 보낼 수 있는 박스 확인
    for i in range(m):
        # 최대 용량
        temp = c
        for j in range(boxes[i][0], boxes[i][1]):
            # 보내는 마을에서 받는 마을까지 보낼 수 있는 최대 용량
            temp = min(temp, delivery[j], boxes[i][2])
        # 보내고 난 후 남은 용량
        for j in range(boxes[i][0], boxes[i][1]):
            delivery[j] -= temp
        result += temp

    print(result)


if __name__ == '__main__':
    solution(n, c)
