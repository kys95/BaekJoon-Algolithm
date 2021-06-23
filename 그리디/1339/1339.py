import sys
input = sys.stdin.readline

# 단어 갯수 n입력
n = int(input().rstrip())
# 단어 저장할 배열
words = []
# 단어 입력
for _ in range(n):
  words.append(list(input().rstrip()))

# 딕셔너리에 알맞은 알파벳, 숫자 넣기
dict = {}
for word in words:
  length = len(word) - 1
  # 단어의 알파벳 확인
  for alphabet in word:
    # 중복일 때
    if alphabet in dict:
      dict[alphabet] += 10 ** length
    # 처음일 때
    else:
      dict[alphabet] = 10 ** length
    # 자릿수 감소
    length -= 1

# value값만 넣음
arr = []
for value in dict.values():
  arr.append(value)
# 내림차순 정렬
arr = sorted(arr, reverse=True)

# 최종출력할 값, 매핑할 숫자
result = 0
mapping = 9

for num in arr:
  result += num * mapping
  mapping -= 1
print(result)