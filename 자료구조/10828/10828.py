import sys
n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0] #명령어 받기

    #word의 값에 따라 역할을 수행하기

    #order가 push라면
    if order == "push":
        value = word[1]
        stack.append(value)

    #order가 pop이라면
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #order가 size라면
    elif order == "size":
        print(len(stack))

    #order가 empty라면
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #order가 top이라면
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])