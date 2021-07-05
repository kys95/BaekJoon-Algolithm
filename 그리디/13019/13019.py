s=input()
t=input()
if sorted(s) != sorted(t):
    print(-1)
    exit(0)
c=len(t)
for i in s[::-1]:
    if i==t[c-1]:
        c-=1
print(c)