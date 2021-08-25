# n 가지 종류, 합 -> k 원
# 최소한의 개수는?
# 불가능한 경우는 -1
n, k = map(int, input().split())
coins = []
dp = [10001] * (k + 1)
dp[0] = 0
for i in range(n):
    coins.append(int(input()))

coins.sort()
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])