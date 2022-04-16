# 問題:AtCoder Beginner Contest 007 C - 幅優先探索
# 問題URL:https://atcoder.jp/contests/abc007/tasks/abc007_3
# 解法URL:https://atcoder.jp/contests/abc007/submissions/30959755

import math
from collections import deque

r, c = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
map_list = []
for _ in range(r):
    map_list.append(input())

path = [[] for _ in range((r - 2) * (c - 2))]
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if map_list[i][j] == '.':
            if map_list[i][j + 1] == '.':
                path[(i - 1) * (c - 2) + (j - 1)].append((i - 1) * (c - 2) + j)
                path[(i - 1) * (c - 2) + j].append((i - 1) * (c - 2) + (j - 1))
            if map_list[i + 1][j] == '.':
                path[(i - 1) * (c - 2) + (j - 1)].append(i * (c - 2) + (j - 1))
                path[i * (c - 2) + (j - 1)].append((i - 1) * (c - 2) + (j - 1))

dist = [math.inf] * ((r - 2) * (c - 2))
d = deque()
dist[(start_y - 2) * (c - 2) + (start_x - 2)] = 0
d.append((start_y - 2) * (c - 2) + (start_x - 2))

while d:
    v = d.popleft()
    for i in path[v]:
        if dist[i] > dist[v] + 1:
            dist[i] = dist[v] + 1
            d.append(i)
        else:
            continue

print(dist[(goal_y - 2) * (c - 2) + (goal_x - 2)])
