if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  stk = []
  result = [-1 for _ in range(n)]
  for i in range(n):
    while stk and arr[stk[-1]] < arr[i]:
      result[stk[-1]] = arr[i]
      stk.pop(-1)
    stk.append(i)

  print(' '.join(map(str, result)))

# 1. -1을 n개만큼 만들어 배열 result을 만든다.
# 2. 스택의 가장 바닥에는 스택 내에 가장 오래된 인덱스가 놓이게 되고 스택의 바닥값의 arr과 arr[i]을 비교하여 result를 갱신한다.