# 問題:JOI 2012 予選 4 - パスタ
# 問題URL:https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
# 解法URL:https://atcoder.jp/contests/joi2012yo/submissions/30768979

n, k = map(int, input().split())
shitei = []
for i in range(k):
    a = list(map(int, input().split()))
    a[1] -= 1
    shitei.append(a)

dp = [[[0, 0] for i in range(3)] for l in range(n)]

for i in range(3):
    dp[0][i][0] = 1

for i in range(k):
    if shitei[i][0] == 1:
        dp[0][shitei[i][1]][0] = 1
        for l in range(3):
            if shitei[i][1] != l:
                dp[0][l][0] = 0

for i in range(1, n):
    for l in range(3):
        dp[i][l][1] = dp[i - 1][l][0]
        temp = 0
        for j in range(3):
            if l != j:
                temp += dp[i - 1][j][0]
                temp += dp[i - 1][j][1]

        dp[i][l][0] = temp % 10000

    for l in range(k):
        if shitei[l][0] - 1 == i:
            for j in range(3):
                if shitei[l][1] != j:
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0

ans = 0
for i in range(3):
    ans += dp[n - 1][i][0]
    ans += dp[n - 1][i][1]

print(ans % 10000)
