if __name__ == "__main__":
  n, m = map(int, input().split())
  arr = [list(map(int, input())) for _ in range(n)]
  answer = max(arr[0])
  for i in range(1, n):
    for j in range(1, m):
      if arr[i][j] == 1:
        arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j]) + 1

    answer = max(answer, max(arr[i]))

  print(answer**2)

# 1. dp[i][j]를 (i,j)칸을 우하단으로 삼는 가장 큰 정사각형의 한 변의 길이라고 한다.
# 2. (1,1) ~ (n-1,m-1)을 우하단으로 가정하여 왼쪽, 위쪽, 왼쪽대각선 위인 인접한 세 칸을 확인하여 가장 작은 수 + 1을 한다.
#    즉, 2x2 정사각형이 되기위해서는 최소 1, 3x3 정사각형이 되기위해서는 최소 2가 인접한 세칸이어야 한다.
# 3. arr의 원소들을 갱신한 후 가장 큰 값의 제곱을 출력한다.