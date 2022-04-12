# 問題:AtCoder Beginner Contest 023 D - 射撃王
# 問題URL:https://atcoder.jp/contests/abc023/tasks/abc023_d
# 解法URL:https://atcoder.jp/contests/abc023/submissions/30924448

n = int(input())

h = []
s = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    h.append(tmp[0])
    s.append(tmp[1])


def is_ok(x):
    flag = True
    lim_time = []
    for i in range(len(h)):
        lim_time.append((x - h[i]) / s[i])
    lim_time.sort()
    for i in range(len(lim_time)):
        if i <= lim_time[i]:
            pass
        else:
            flag = False

    return flag


right = 10 ** 19
left = 0
while left + 1 < right:
    mid = (left + right) // 2
    if is_ok(mid):
        right = mid
    else:
        left = mid

print(right)
