K = int(input())
num_stack = []

for _ in range(K):
    n = int(input())
    if n == 0:
        num_stack.pop()
    else:
        num_stack.append(n)

result = sum(num_stack)
print(result)