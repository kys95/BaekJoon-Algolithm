import sys
input = sys.stdin.readline
from itertools import combinations

people = []
for _ in range(9):
  people.append(int(input()))

choices = list(combinations(people, 7))


for choice in choices:
  if sum(choice) == 100:
    choice = sorted(choice)
    for x in choice:
      print(x)
    break