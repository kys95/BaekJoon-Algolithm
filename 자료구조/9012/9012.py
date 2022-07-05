n = int(input())
for _ in range(n):
  data = input()
  stack = []
  ans = 'YES'
  for c in data:
    if c == "(":
      stack.append(c)
    else:
      if len(stack) > 0:
        stack.pop()
      else:
        ans = 'NO'
  if len(stack) > 0:
    ans = 'NO'
  print(ans)