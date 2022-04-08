# 問題:JOI 2011 予選 4 - 1 年生
# 問題URL:https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
# 解法URL:https://atcoder.jp/contests/joi2011yo/submissions/30753238

n = int(input())
suuretu = list(map(int, input().split()))
ans = suuretu.pop()

dp = [[0] * 21 for i in range(n - 1)]
dp[0][suuretu[0]] = 1

for i in range(n - 2):
    for l in range(21):
        if dp[i][l] != 0:
            if l + suuretu[i + 1] <= 20:
                dp[i + 1][l + suuretu[i + 1]] += dp[i][l]
            if l - suuretu[i + 1] >= 0:
                dp[i + 1][l - suuretu[i + 1]] += dp[i][l]

print(dp[n - 2][ans])
