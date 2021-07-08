import sys
input = sys.stdin.readline

# 볼의 총갯수 n 입력
n = int(input().rstrip())
# 볼 색깔 입력
balls = list(input().rstrip())
# B볼의 갯수, R볼의 갯수
B_count = balls.count('B')
R_count = n - B_count

def move(color, balls):
    global B_count, R_count
    # 원하는 색깔의 공 옮기는 횟수
    count = 0
    # 무더기 찾기
    for ball in balls:
        if ball != color:
            if color == 'B':
                return B_count - count
            else:
                return R_count - count
        count += 1
    # 색깔이 모두 같다면 0 리턴
    return 0

if __name__ == '__main__':
    # B볼을 오른쪽,왼쪽으로 옮기는 경우 & R볼을 오른쪽,왼쪽으로 옮기는 경우 -> 4가지
    print(min(move('B', balls[::-1]), move('B', balls[:]), move('R', balls[::-1]), move('R', balls[:])))