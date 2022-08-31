if __name__ == "__main__":
  n = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A.sort()
  B.sort(reverse=True)

  result = 0
  for i in range(n):
    result += A[i] * B[i]
  print(result)

# 1. A와 B의 원소들의 곱의 최소값을 구하는 문제이다.
# 2. A와 B를 오름차순,내림차순 or 내림차순,오름차순으로 서로 다르게 정렬하여 각 원소끼리 곱해준다.