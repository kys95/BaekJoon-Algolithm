from itertools import combinations

n, m = map(int, input().split())
# 집, 치킨집
house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:  # 집
            house.append((i, j))
        elif data[j] == 2:  # 치킨집
            chicken.append((i, j))
# 치킨집 중 m개의 조합
chicken_list = list(combinations(chicken, m))


# 최소치킨거리
def get_sum(house, data):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in data:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result


result = 1e9
for data in chicken_list:
    result = min(result, get_sum(house, data))
print(result)
