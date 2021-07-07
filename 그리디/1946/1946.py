import sys
input = sys.stdin.readline

def solution():
    # 서류성적 기준 오름차순 정렬
    people.sort(key=lambda x: x[0])
    # 신입사원 인원수 1로 초기화(첫 번째는 무조건 합격)
    count = 1
    # 면접성적 기준
    std = people[0][1]
    # 면접성적 기준보다 높으면 합격
    for i in range(1, len(people)):
        if people[i][1] < std:
            std = people[i][1]
            count += 1
    print(count)

if __name__ == '__main__':
    # 테스트 케이스 k 입력
    k = int(input().rstrip())
    for _ in range(k):
        # 지원자 숫자 n 입력
        n = int(input().rstrip())
        # 지원자 순위 담을 리스트
        people = []
        # 지원자 서류성적, 면접성적 입력
        for _ in range(n):
            a, b = map(int, input().split())
            people.append((a, b))

        solution()
