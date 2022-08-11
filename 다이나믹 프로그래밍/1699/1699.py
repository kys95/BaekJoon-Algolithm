if __name__ == "__main__":
  n = int(input())
  dp = [i for i in range(n + 1)]

  for i in range(4, n + 1):
    for j in range(1, i):
      if i < j * j:
        break

      if dp[i] > dp[i - j * j] + 1:
        dp[i] = dp[i - j * j] + 1

  print(dp[n])

# 1. f(i) = 'i를 제곱수들의 합으로 나타냈을 때 항의 최소 개수'라고 정의하면 구하는 답은 f(N)이다.
#    i에서 1<sup>2</sup>을 뺐을 때, 2<sup>2</sup>을 뺐을 때 .. 각각의 경우를 살펴보고 그 중에 가장 항이 최소개수일 때를 찾으면 된다.
# 2. 따라서 점화식은 f(i) = min(f(i-1<sup>2</sup>),f(1-2<sup>2</sup>),...,f(i-j<sup>2</sup>)) + 1