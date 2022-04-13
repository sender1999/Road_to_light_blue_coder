# 問題:ALDS_11_C - 幅優先探索
# 問題URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
# 解法URL:https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=6482376#1

from collections import deque

n = int(input())

path = [[]]

for _ in range(n):
    tmp = list(map(int, input().split()))
    path.append(tmp[2:])

dist = [-1] * (n+1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in path[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

ans = dist[1:]
for i, j in enumerate(ans):
    print("{} {}".format(i+1, j))
