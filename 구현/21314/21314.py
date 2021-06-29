import sys

input = sys.stdin.readline

# 민겸 수 입력
arr = list(input().rstrip())


# 최대
def find_max():
    big = ''
    # 연속된 M 카운트 변수
    count_of_M = 0
    for i in range(len(arr)):
        # 문자가 K라면
        if arr[i] == 'K':
            big += str(5 * (10 ** count_of_M))
            count_of_M = 0
        else:
            count_of_M += 1
            # 끝자리가 M일 경우
            if i == len(arr) - 1:
                big += '1' * count_of_M
    print(big)


# 최소
def find_min():
    small = ''
    # 연속된 M 카운트 변수
    count_of_M = 0
    for i in range(len(arr)):
        # 문자가 K라면
        if arr[i] == 'K':
            # 5추가
            small += '5'
            # 카운트 변수 0으로 초기화
            count_of_M = 0
        # 문자가 M이라면
        else:
            count_of_M += 1
            # 연속된 M의 갯수에 따라
            if count_of_M == 1:
                small += '1'
            else:
                small += '0'

    print(small)


find_max()
find_min()
