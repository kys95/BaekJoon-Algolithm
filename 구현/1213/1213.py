from collections import Counter

if __name__ == "__main__":
  alpha_cnt = Counter(input())
  if sum(cnt % 2 for cnt in alpha_cnt.values()) > 1:
    print("I'm Sorry Hansoo")
  else:
    half = ''
    for alpha, cnt in sorted(alpha_cnt.items()):
      half += alpha * (cnt // 2)

    result = half
    for alpha, cnt in sorted(alpha_cnt.items()):
      if cnt % 2:
        result += alpha

    result += ''.join(reversed(half))
    print(result)

# 1. Counter를 이용하여 각 문자의 개수를 딕셔너리 형태로 받는다.
# 2. 좌우 대칭이어야 하므로 홀수개인 문자의 개수가 2개이상이면 예외 처리 해준다.
# 3. 딕셔너리 형태로 받은 alpha_cnt를 알파벳 순으로 정렬하고 앞에서 부터 절반씩 추가한다.
# 4. 홀수인 문자를 가운데에 추가하고 앞에서 부터 추가한 절반 문자열을 뒤집은 것을 추가한다.