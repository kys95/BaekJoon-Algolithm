import sys
input = sys.stdin.readline

# 나무의 갯수 n 입력
n = int(input().rstrip())
# 나무 정보 담을 리스트
trees = []
# 나무 길이 입력
one = list(map(int, input().split()))
# 자라는 길이 입력
two = list(map(int, input().split()))
# 리스트에 (나무 길이, 자라는 길이)  입력
for i in range(n):
  trees.append((one[i], two[i]))

def solution(n):
  # 자라는 길이가 작은 것부터 큰 순서대로 오름차순 정렬
  trees.sort(key =lambda x:x[1])
  # 나무 자르는 양
  result = 0
  for i in range(n):
    result += trees[i][0] + i * trees[i][1]
  print(result)

if __name__ == '__main__':
  solution(n)