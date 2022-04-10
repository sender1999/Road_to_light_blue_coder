# 問題:ALDS_11_B - 深さ優先探索
# 問題URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
# 解法URL:https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=6471354#1

N = int(input())

path = list()
path.append([])

for _ in range(N):
    tmp = list(map(int, input().split()))
    path.append(tmp[2:])

d = [0]*(N+1)
f = [0]*(N+1)

TIME = 0

def dfs(p, d, f):
    global TIME

    TIME += 1
    d[p] = TIME

    for i in path[p]:
        if d[i] == 0:
            dfs(i, d, f)

    TIME += 1
    f[p] = TIME

    return

for start in range(1, N+1):
    if d[start] == 0:
        dfs(start, d, f)

for i in range(1, N+1):
    print(i, d[i], f[i])
