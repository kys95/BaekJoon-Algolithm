from itertools import product
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
operations = list(product(['+', '-', '*', '/'], repeat=(n - 1)))


max_value = -1e9
min_value = 1e9

for operation in operations:
  result = numbers[0]
  if operation.count('+') == add and operation.count('-') == sub and operation.count('*') == mul and operation.count('/') == div:
    for i in range(n - 1):
      if operation[i] == '+':
        result += numbers[i + 1]
      if operation[i] == '-':
        result -= numbers[i + 1]
      if operation[i] == '*':
        result *= numbers[i + 1]
      if operation[i] == '/':
        result = int(result / numbers[i + 1])
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)