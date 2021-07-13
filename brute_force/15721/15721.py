import sys

input = sys.stdin.readline

# 게임참여자수 n 입력
n = int(input().rstrip())
# 구하고자 하는 번째  t 입력
t = int(input().rstrip())
# 구하고자 하는 구호
say = input().rstrip()


def solution(n, t, say):
    # 게임 참여자가 1명일 경우
    if n == 1:
        return 0  # 어떤것이든 본인이
    else:
        bbun_count = 0  # 뻔 카운트 변수
        daegi_count = 0  # 데기 카운트 변수
        cnt = 0  # 회차

        while True:
            cnt += 1  # 회차 + 1
            for i in range(4):          # 공통
                if i % 2 == 0:
                    bbun_count += 1
                else:
                    daegi_count += 1

                if bbun_count == t and say == '0':
                    return (bbun_count + daegi_count - 1) % n
                elif daegi_count == t and say == '1':
                    return (bbun_count + daegi_count - 1) % n

            for i in range(cnt + 1):                # 회차에 따른 뻔 추가
                bbun_count += 1
                if bbun_count == t and say == '0':
                    return (bbun_count + daegi_count - 1) % n

            for i in range(cnt + 1):                # 회차에 따른 데기 추가
                daegi_count += 1
                if daegi_count == t and say == '1':
                    return (bbun_count + daegi_count - 1) % n


if __name__ == "__main__":
    print(solution(n, t, say))