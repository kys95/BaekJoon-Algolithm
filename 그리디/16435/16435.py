import sys
input = sys.stdin.readline

# 과일 갯수 N, 스네이크버드 초기길이 L 입력
N, L = map(int, input().split())
# 과일 높이 입력
fruits = list(map(int, input().split()))

def solution(length):
  # 과일 높이 오름차순 정렬
  fruits.sort()
  # 초기길이와 과일 높이 비교
  for fruit in fruits:
    if length >= fruit:
      length += 1
    else:
      break
  print(length)

if __name__ == '__main__':
  solution(L)