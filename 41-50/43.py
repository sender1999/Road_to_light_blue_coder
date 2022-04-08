# 問題:パ研杯2019 D - パ研軍旗
# 問題URL:https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
# 解法URL:https://atcoder.jp/contests/pakencamp-2019-day3/submissions/30786376

import math

N = int(input())

flag = []
for i in range(5):
    flag.append(input())

dp = [[math.inf] * 3 for i in range(N)]

for i in range(N):
    red = 5
    blue = 5
    white = 5
    for j in range(5):
        tmp = flag[j][i]
        if tmp == 'R':
            red -= 1
        elif tmp == 'B':
            blue -= 1
        elif tmp == 'W':
            white -= 1
    if i == 0:
        dp[0][0] = red
        dp[0][1] = blue
        dp[0][2] = white
    else:
        dp[i][0] = red + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = blue + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = white + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))
