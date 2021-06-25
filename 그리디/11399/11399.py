n = int(input())
pi = list(map(int, input().split()))
pi.sort()
sum = 0

for i in range(n):
    sum += pi[i] * (n - i)
print(sum)