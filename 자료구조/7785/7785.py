if __name__ == "__main__":
  n = int(input())
  company = set()
  for _ in range(n):
    data = input()
    p, s = data.split()
    if s == "enter":
      company.add(p)
    else:
      company.remove(p)

  company = list(company)
  company = sorted(company, reverse=True)
  for p in company:
    print(p)