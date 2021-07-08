import sys
input = sys.stdin.readline

# 사과나무 갯수 n 입력
n = int(input().rstrip())
# 사과나무 높이 입력
trees = list(map(int, input().split()))

def solution():
    # 사과나무 높이 총합
    height = sum(trees)
    # 3의 배수가 아니라면 "NO"
    if height % 3 != 0:
        print("NO")

    else:
        # 2가 들어가는 갯수
        count_of_2 = height // 3
        # 사과나무 높이에서 2가 들어가는 갯수 확인
        for tree in trees:
            count_of_2 -= tree // 2
        # 2의 갯수 충족 x
        if count_of_2 > 0:
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    solution()