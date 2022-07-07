if __name__ == "__main__":
  n = int(input())
  oper = input()
  nums = []
  for _ in range(n):
    nums.append(int(input()))
  stk = []
  for op in oper:
    if op.isalpha():  #문자면 숫자로 대입
      stk.append(nums[ord(op)- ord('A')])
    else:
      b = stk.pop()
      a = stk.pop()
      if op == '+':
        stk.append(a + b)
      elif op == '*':
        stk.append(a * b)
      elif op == '/':
        stk.append(a / b)
      elif op == '-':
        stk.append(a - b)

  print(f'{stk.pop():.2f}')