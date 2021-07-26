import sys
input = sys.stdin.readline

# n 입력
n = int(input().rstrip())
# 교실(그래프) 초기화
graph = [[0] * n for _ in range(n)]
# 학생 정보 담을 리스트
students = []
# 자리잡은 학생 담을 딕셔너리
dic = {}
# 학생 정보입력
for _ in range(n ** 2):
    students.append(list(map(int, input().split())))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(friends, i, j):
    count = 0
    f_count = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                count += 1
            if friends:
                if graph[nx][ny] in friends:
                    f_count += 1

    return count, f_count

if __name__ == "__main__":
    # 학생 차례대로 탐색
    for student in students:
        friends = []
        for i in range(1, 5):
            if student[i] in dic:
                friends.append(student[i])

        # 좋아하는 학생 한명이라도 자리 잡은 경우
        if friends:
            max_lis = []
            for i in range(n):
                for j in range(n):
                    if graph[i][j] == 0:
                        result, f_result = solution(friends, i, j)

                        if not max_lis:
                            max_lis = [f_result, result, i, j]
                        elif max_lis[0] < f_result:
                            max_lis = [f_result, result, i, j]
                        elif max_lis[0] == f_result and max_lis[1] < result:
                            max_lis = [f_result, result, i, j]

            # 자리 선택
            graph[max_lis[2]][max_lis[3]] = student[0]
            dic[student[0]] = student[1:]


        # 좋아하는 학생 모두 자리잡지 못한 경우
        else:
            max_lis = []
            for i in range(n):
                for j in range(n):
                    if graph[i][j] == 0:
                        result, f_result = solution(friends, i, j)

                        if not max_lis:
                            max_lis = [result, i, j]
                        elif max_lis[0] < result:
                            max_lis = [result, i, j]

            # 자리 선택
            graph[max_lis[1]][max_lis[2]] = student[0]
            dic[student[0]] = student[1:]

    # 다 앉힌 후에 점수를 계산
    # 0:0 / 1:1 / 2:10 / 3:100 / 4:1000
    point = 0
    for i in range(n):
        for j in range(n):
            f_list = dic[graph[i][j]]
            empty_val, f_cnt = solution(f_list, i, j)
            if f_cnt == 0:
                point += 0
            elif f_cnt == 1:
                point += 1
            elif f_cnt == 2:
                point += 10
            elif f_cnt == 3:
                point += 100
            else:
                point += 1000

    print(point)