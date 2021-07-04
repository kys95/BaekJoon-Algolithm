import sys
input = sys.stdin.readline

# 레벨의 수 n입력
n = int(input().rstrip())
# 레벌 점수 담을 리스트
scores = []
# 레벨 점수 입력
for _ in range(n):
  scores.append(int(input().rstrip()))


def solution():
  # 레벨 점수 뒤집기
  scores.reverse()
  # 감소시킬 레벨점수
  result = 0
  # 감소시켜야 할 레벨점수가 있는지 확인
  for i in range(1, len(scores)):
    if scores[i] >= scores[i - 1]:
      # 감소시킬 레벨점수 누적합
      result += (scores[i] - scores[i - 1] + 1)
      # 레벨 점수 변경
      scores[i] = scores[i - 1] - 1
  print(result)


if __name__ == '__main__':
  solution()