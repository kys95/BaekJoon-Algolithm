from itertools import combinations

if __name__ == "__main__":
    nanjang = []
    for _ in range(9):
        nanjang.append(int(input()))
    target = 100
    answer = []
    for option in list(combinations(nanjang, 7)):
        if sum(option) == target:
            answer = option
            break

    for x in answer:
        print(x)