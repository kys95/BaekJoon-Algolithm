# 학생n명 입력
n = int(input())
# (이름, 국어점수, 영어점수, 수학점수)정보 입력받을 리스트
students = []
for i in range(n):
    data = input().split()
    students.append((data[0], int(data[1]), int(data[2]), int(data[3])))
# 국어점수 감소, 영어점수 증가, 수학점수 감소, 이름사전순 증가 순으로 정렬
students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 학생이름 출력
for student in students:
    print(student[0])