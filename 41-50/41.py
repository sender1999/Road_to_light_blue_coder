# 問題:JOI 2013 予選 4 - 暑い日々
# 問題URL:https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
# 解法URL:https://atcoder.jp/contests/joi2013yo/submissions/30775672

D, N = map(int, input().split())
temperature = []
for i in range(D):
    temperature.append(int(input()))
clothes = []
for i in range(N):
    clothes.append(list(map(int, input().split())))

dp = [[-1] * N for i in range(D)]

for i in range(N):
    today_temp = temperature[0]
    if clothes[i][0] <= today_temp & today_temp <= clothes[i][1]:
        dp[0][i] = 0

for i in range(D-1):
    today_temp = temperature[i+1]
    for l in range(N):
        if dp[i][l] != -1:
            for j in range(N):
                if clothes[j][0] <= today_temp & today_temp <= clothes[j][1]:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][l]+abs(clothes[l][2]-clothes[j][2]))

print(max(dp[D-1]))
