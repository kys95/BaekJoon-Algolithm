# 집의 수 n 입력
n = int(input())
# 집의 위치 입력
house = list(map(int, input().split()))
# 오름차순 정렬
house = sorted(house)
# 안테나 설치 위치 출력
print(house[(len(house) - 1) // 2])