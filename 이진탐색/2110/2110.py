import sys
input = sys.stdin.readline

# 이진탐색을 이용한 두 공유기 사이의 최대거리 계산
def find_distance(house, target, start, end):
    # 가장 인접한 두 공유기 사이의 최대거리
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # 공유기 설치 갯수
        count = 1
        # 공유기 처음 설치 집 좌표
        gong_yu_gi = house[0]
        # 순서대로 공유기 설치
        for i in range(1, n):
            # 공유기 설치 가능하다면
            if house[i] >= gong_yu_gi + mid:
                # 설치 갯수 계산
                count += 1
                gong_yu_gi = house[i]
        # 설치해야 하는 공유기 갯수보다 크거나 같다면
        if count >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

# 집의 갯수 n, 공유기의 갯수 c입력
n, c = map(int, input().split())
# 집의 좌표를 담을 리스트
house = []
# n개의 집 좌표 입력
for i in range(n):
  data = int(input().rstrip())
  house.append(data)
# 오름차순 정렬
house = sorted(house)
# 가능한 두 공유기 사이의 최솟값
start = 1
# 가능한 두 공유기 사이의 최댓값
end = house[n - 1]
result = find_distance(house, c, start, end)
print(result)