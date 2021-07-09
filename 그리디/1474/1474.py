import sys
input = sys.stdin.readline

def solution(base, add):
    # 최종 출력 단어
    result = ''
    # 균등하게 넣을 밑줄 갯수가 없다면
    if base == 0:
        result = '_'.join(words)
        print(result[:m])
    else:
        for i in range(n):
            # 첫단어 x & 밑줄 추가 갯수 남아있음 & 소문자 고려
            if i != 0 and arr[i] == 0 and add > 0:
                result += '_'  # 밑줄 추가
                add -= 1  # 밑줄 추가 갯수 감소
            # 첫단어 x & 밑줄 추가 갯수 남아있음 & 대문자 고려
            elif i != 0 and add > 0 and n - i <= add:
                result += '_'
                add -= 1
            # 균등하게 넣을 밑줄 갯수 고려
            result += (words[i] + '_' * base)
        # 마지막 단어오른쪽에 넣은 밑줄 삭제
        for _ in range(base):
            result = result[:-1]
        # 최종 출력
        print(result)

if __name__ == '__main__':
    # 단어갯수 n, 만들고자 하는 최종 길이 m 입력
    n, m = map(int, input().split())
    # 단어 입력받을 리스트
    words = []
    # 각 단어들의 첫문자가 대문자or소문자인지 판단하는 정보입력 리스트
    arr = []
    # 입력받은 단어의 총 길이
    length = 0
    # n개의 단어 입력
    for _ in range(n):
        data = input().rstrip()
        length += len(data)
        arr.append(data[0].isupper())
        words.append(data)

    # 단어사이마다 균등하게 넣을 밑줄 갯수
    base = (m - length) // (n - 1)
    # 밑줄 추가 갯수
    add = (m - length) % (n - 1)
    solution(base, add)