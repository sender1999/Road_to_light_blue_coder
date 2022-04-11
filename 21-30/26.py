# 問題:AtCoder Beginner Contest 138 D - Ki
# 問題URL:https://atcoder.jp/contests/abc138/tasks/abc138_d
# 解法URL:https://atcoder.jp/contests/abc138/submissions/30904880

import sys
# Pythonには再帰関数の再帰回数が制限されてるので制限を増やす。
sys.setrecursionlimit(10 ** 9)

N, Q = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

counter = [0] * (N + 1)
for _ in range(Q):
    p, x = map(int, input().split())
    counter[p] += x

seen = [-1] * (N + 1)


def dfs(p, seen, counter):
    seen[p] = 0

    for nxt in path[p]:
        if seen[nxt] == -1:
            counter[nxt] += counter[p]
            dfs(nxt, seen, counter)

    return


dfs(1, seen, counter)

print(*counter[1:])
