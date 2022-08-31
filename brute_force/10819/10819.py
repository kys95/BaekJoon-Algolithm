from itertools import permutations

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  result = 0

  for choice in set(permutations(arr, n)):
    temp = 0
    for i in range(1, n):
      temp += abs(choice[i - 1] - choice[i])
    result = max(result, temp)

  print(result)

# 1. n이 최대가 8이므로 permutations를 이용하여 완전탐색을 이용해도 무방하다.
# 2. 입력받은 배열 arr의 모든 경우의 수를 구하고 최대값을 찾는다.