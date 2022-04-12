# 問題:AtCoder Beginner Contest 077 C - Snuke Festival
# 問題URL:https://atcoder.jp/contests/abc077/tasks/arc084_a
# 解法URL:https://atcoder.jp/contests/abc077/submissions/30922448

import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.append(0)
a.append(math.inf)
c.append(0)
c.append(math.inf)

a.sort()
b.sort()
c.sort()


def binary_search_a(target, s):
    left = 0
    right = len(s) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if s[mid] < target:
            left = mid
        else:
            right = mid
    return left


def binary_search_c(target, s):
    left = 0
    right = len(s) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if s[mid] > target:
            right = mid
        else:
            left = mid
    return right


ans = 0

for i in range(n):
    a_max = binary_search_a(b[i], a)
    c_min = binary_search_c(b[i], c)
    ans += a_max * (n - c_min + 1)

print(ans)
