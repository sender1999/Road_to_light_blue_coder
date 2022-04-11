# 問題:JOI 2009 予選 4 - 薄氷渡り
# 問題URL:https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
# 解法URL:

import sys

sys.setrecursionlimit(10 ** 9)

M = int(input())
N = int(input())

ice_map = []

for _ in range(N):
    ice_map.append(list(map(int, input().split())))

path = [[] for _ in range(N * M + 1)]

for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 1:
            if j != M - 1:
                if ice_map[i][j + 1] == 1:
                    path[i * M + j + 1].append(i * M + (j + 1) + 1)
                    path[i * M + (j + 1) + 1].append(i * M + j + 1)
            if i != N - 1:
                if ice_map[i + 1][j] == 1:
                    path[i * M + j + 1].append((i + 1) * M + j + 1)
                    path[(i + 1) * M + j + 1].append(i * M + j + 1)


def dfs(p, seen, cnt, cr_max):
    cnt += 1
    cr_max = max(cnt, cr_max)
    seen[p] = 1
    for nxt in path[p]:
        if seen[nxt] == 0:
            cr_max = dfs(nxt, seen, cnt, cr_max)
    cnt -= 1
    return cr_max


ans = -1
for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 1:
            seen = [0] * (N * M + 1)
            ans = dfs(i * M + j + 1, seen, 0, ans)

print(ans)
