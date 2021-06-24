import sys
input = sys.stdin.readline

# 나무수 n, 가져가려고 하는 나무길이 m
n, m = map(int, input().split())
# n개의 나무 배열 입력
trees = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝
start = 0
end = max(trees)

# 이진탐색 수행
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for tree in trees:
    # 잘랐을 때 나무 길이 계산
    if tree > mid:
      total += tree - mid

  # 나무 길이가 짧은 경우 왼쪽 탐색
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)