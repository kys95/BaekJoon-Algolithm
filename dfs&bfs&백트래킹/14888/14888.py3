n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
# 최대, 최소
max_val = -1e9
min_val = 1e9

def dfs(i, num, add, sub, mul, div):
  global max_val, min_val
  if i == n:
    max_val = max(max_val, num)
    min_val = min(min_val, num)
    return 
  else:
    if add:
      dfs(i + 1, num + numbers[i], add - 1, sub, mul, div)
    if sub:
      dfs(i + 1, num - numbers[i], add, sub - 1, mul, div)
    if mul:
      dfs(i + 1, num * numbers[i], add, sub, mul - 1, div)
    if div:
      dfs(i + 1, int(num / numbers[i]), add, sub, mul, div - 1)
  
dfs(1, numbers[0], add, sub, mul, div)
print(max_val)
print(min_val)