# 問題:JOI 2010 本選 1 - 旅人
# 問題URL:https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a
# 解法URL:https://atcoder.jp/contests/joi2010ho/submissions/30801817

N, M = map(int, input().split())

s = [0]
for i in range(N-1):
    s.append(s[i]+int(input()))

p = 0
ans = 0
for i in range(M):
    t = int(input())
    ans += abs(s[p+t]-s[p])
    p += t

print(ans % 10**5)
