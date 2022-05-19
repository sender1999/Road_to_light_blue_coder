# 問題:AtCoder Beginner Contest 128 C - Switches
# 問題URL:https://atcoder.jp/contests/abc128/tasks/abc128_c
# 解法URL:https://atcoder.jp/contests/abc128/submissions/31793715

N, M = map(int, input().split())
s = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    s.append(tmp[1:])
p = list(map(int, input().split()))

ALL = 1 << N


def has_bit(n, i):
    return n & (1 << i) > 0


ans = 0
for i in range(ALL):
    flag = [False]*M
    for j in range(M):
        tmp = 0
        for k in s[j]:
            if has_bit(i, k-1):
                tmp += 1
        if tmp % 2 == p[j]:
            flag[j] = True
    if sum(flag) == M:
        ans += 1

print(ans)
