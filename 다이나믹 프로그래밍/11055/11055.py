if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [num for num in arr]

    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])

    print(max(dp))