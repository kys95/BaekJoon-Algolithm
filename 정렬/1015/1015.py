if __name__ == "__main__":
  n = int(input())
  A = list(map(int, input().split()))
  B = sorted([val, idx] for idx, val in enumerate(A))
  dp = [-1] * n

  for idx, pair in enumerate(B):
    dp[pair[1]] = idx

  print(' '.join(map(str, dp)))


# 1. A의 인덱스 idx, 원소값 val을 원소로 하고 val을 기준으로 오름차순 정렬된 B를 초기화한다.
# 2. B기준에서 A의 val의 인덱스값을 저장하는 dp를 -1로 초기화한다.
# 3. A의 인덱스 순서대로 B의 val과 일치하는 인덱스 값을 dp에 넣는다.
