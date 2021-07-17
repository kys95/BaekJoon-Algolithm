import sys
input = sys.stdin.readline
from itertools import combinations

# 회원수 n, 치킨 종류 m 입력
n, m = map(int, input().split())
# 치킨 선호도 저장할 리스트
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))

def solution(choice):
    global result

    count = 0
    for i in range(n):
        temp = 0
        for data in choice:
            if temp < people[i][data]:
                temp = people[i][data]
        count += temp
    result = max(result, count)

if __name__ == "__main__":
    result = 0
    # 1~3개 뽑는 조합
    for i in range(1, 4):
        choices = combinations(list(range(m)), i)
        for choice in choices:
            solution(choice)
    print(result)