from collections import deque
import copy
import sys
input = sys.stdin.readline

# 모두 같은 면인지 확인
def check(temp):
    return len(set(''.join(sum(temp, [])))) == 1  # 모두 같은면이면 True 반환

def solution(coins):
    # 큐
    que = deque([coins])
    # 집합 자료형(중복 확인 하기 위함)
    result = set()
    result.add(''.join(sum(coins, [])))
    # 연산 횟수
    count = 0

    while que:
        length = len(que)
        for _ in range(length):
            temp = que.popleft()
            if check(temp):
                return count

            # 행, 열 뒤집기
            for i in range(3):
                temp1 = copy.deepcopy(temp)
                temp2 = copy.deepcopy(temp)

                # 연산 1개
                for j in range(3):
                    temp1[i][j] = 'H' if temp[i][j] == 'T' else 'T'  # 행
                    temp2[j][i] = 'H' if temp[j][i] == 'T' else 'T'  # 열

                temp1str = ''.join(sum(temp1, []))
                temp2str = ''.join(sum(temp2, []))
                if temp1str not in result:
                    que.append(temp1)
                    result.add(temp1str)
                if temp2str not in result:
                    que.append(temp2)
                    result.add(temp2str)

                # 대각선
                temp3 = copy.deepcopy(temp)
                for i in range(3):
                    temp3[i][i] = 'H' if temp[i][i] == 'T' else 'T'
                temp4 = copy.deepcopy(temp)
                for i in range(3):
                    temp4[2 - i][i] = 'H' if temp[2 - i][i] == 'T' else 'T'

                temp3str = ''.join(sum(temp3, []))
                if temp3str not in result:
                    que.append(temp3)
                    result.add(temp3str)
                temp4str = ''.join(sum(temp4, []))
                if temp4str not in result:
                    que.append(temp4)
                    result.add(temp4str)

        count += 1
    return -1

if __name__ == "__main__":
    # 테스트 케이스 갯수 t입력
    t = int(input().rstrip())
    for _ in range(t):
        # 동전 모양 입력
        coins = []
        for _ in range(3):
            coins.append(list(map(str, input().split())))
        print(solution(coins))