n = int(input())
ans = [1, 2] * (n//2) + ([3] if n%2 else [])
print(*ans)