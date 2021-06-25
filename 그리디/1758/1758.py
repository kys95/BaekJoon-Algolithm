import sys
input = sys.stdin.readline

# 도시 갯수 n 입력
n = int(input().rstrip())
# 받는 팁
tips = []
for _ in range(n):
  tips.append(int(input().rstrip()))

# 내림차순 정렬
tips = sorted(tips, reverse=True)
# 받게 될 최종 팁
result = 0
# 커피받는 순서에 따른 팁 계산
order = 1
for tip in tips:
  tip = tip - (order - 1)
  if tip < 0:
    break
  result += tip
  order += 1
print(result)