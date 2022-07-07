from collections import deque

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        deq1 = deque()
        deq2 = deque()

        for psw in input():

            if psw == '<':  # 커서 왼쪽으로 이동
                if deq1:  # deq1에 문자 존재할 경우
                    deq2.appendleft(deq1.pop())

            elif psw == '>':  # 커서 오른쪽으로 이동
                if deq2:
                    deq1.append(deq2.popleft())

            elif psw == '-':  # 문자 삭제
                if deq1:
                    deq1.pop()

            else:
                deq1.append(psw)


        print(''.join(deq1) + ''.join(deq2))