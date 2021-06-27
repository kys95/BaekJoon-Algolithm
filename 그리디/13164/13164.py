import sys
input = sys.stdin.readline
# n명의 학생, k그룹 입력
n, k = map(int, input().split())
# 키순서대로 입력
person = list(map(int, input().split()))
# 키 차이 저장할 리스트
diff = []
for i in range(n-1):
    diff.append(person[i+1] - person[i])
diff.sort()

answer = 0
for i in range(n-k):
    answer += diff[i]
print(answer)