import sys
input = sys.stdin.readline

def solution(candy):
    # 박스크기 내림차순 정렬
    boxes.sort(reverse=True)
    # 상자 갯수
    count = 0
    for box in boxes:
        # 캔디 다 채울경우
        if candy <= 0:
            break
        candy -= box
        count += 1

    print(count)


if __name__ == '__main__':
    # 테스트 케이스 갯수 t입력
    t = int(input().rstrip())
    # 사탕갯수 j, 박스 갯수 n입력
    for _ in range(t):
        j, n = map(int, input().split())
        # 박스크기 담을 리스트
        boxes = []
        for _ in range(n):
            # 가로, 세로 입력
            x, y = map(int, input().split())
            boxes.append(x * y)

        solution(j)