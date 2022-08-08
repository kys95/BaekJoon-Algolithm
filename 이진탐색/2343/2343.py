def is_possible(mid):
    cnt = 1
    blueray = 0
    for lesson in lessons:
        if blueray + lesson <= mid:
            blueray += lesson
        else:
            cnt += 1
            blueray = lesson

    return cnt <= m


if __name__ == "__main__":
    n, m = map(int, input().split())
    lessons = list(map(int, input().split()))
    left = max(lessons)
    right = sum(lessons)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

        mid = (left + right) // 2

    print(answer)

# 1. 블루레이 크기를 늘리면 늘릴수록 하나의 블루레이에 더 많은 레슨을 담을 수 있다. 그러면 블루레이 개수를 줄일 수 있다.
#    반대로 블루레이 크기를 줄이면 사용하는 블루레이 개수는 늘어난다.
# 2. 블루레이 크기의 최솟값은 max(lessons)이고 최댓값은 sum(lessons)이므로 이 사이에서 블루레이 크기 범위를 조정하며 이분탐색을 한다.
