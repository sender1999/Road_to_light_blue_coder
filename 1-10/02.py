# 問題:AtCoder Beginner Contest 106 B - 105
# 問題URL:https://atcoder.jp/contests/abc106/tasks/abc106_b
# 解法URL:https://atcoder.jp/contests/abc106/submissions/31066239

n = int(input())

ans = 0

for i in range(1, n+1, 2):
    divisor = []
    for j in range(1, n+1):
        if i % j == 0:
            divisor.append(j)
    if len(divisor) == 8:
        ans += 1

print(ans)
