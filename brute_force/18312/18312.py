import sys
input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())

def solution(n, k):
    count = 0
    for hh in range(n + 1):
        if hh < 10:
            hh = '0' + str(hh)

        for mm in range(60):
            if mm < 10:
                mm = '0' + str(mm)

            for ss in range(60):
                if ss < 10:
                    ss = '0' + str(ss)

                if str(k) in str(hh) + str(mm) + str(ss):
                    count += 1
    print(count)

if __name__ == "__main__":
    solution(n, k)