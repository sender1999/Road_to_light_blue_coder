# 問題:JOI 2015 予選 4 - シルクロード
# 問題URL:https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
# 解法URL:https://atcoder.jp/contests/joi2015yo/submissions/30785628

import math

N, M = map(int, input().split())

distance = []
for i in range(N):
    distance.append(int(input()))
condition = []
for i in range(M):
    condition.append(int(input()))

dp = [[math.inf] * (N + 1) for i in range(M + 1)]

dp[0][0] = 0
for i in range(M):
    for j in range(N):
        if dp[i][j] != math.inf:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j != N:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + distance[j] * condition[i])

ans = math.inf
for i in range(M + 1):
    ans = min(ans, dp[i][N])
print(ans)
