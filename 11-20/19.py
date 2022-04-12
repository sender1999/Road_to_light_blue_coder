# 問題:JOI 2009 本選 2 - ピザ
# 問題URL:https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
# 解法URL:https://atcoder.jp/contests/joi2009ho/submissions/30921693

d = int(input())
n_store = int(input())
n_deliv = int(input())
p_store = [0]
for _ in range(n_store - 1):
    p_store.append(int(input()))
p_store.append(d)
p_deliv = []
for _ in range(n_deliv):
    p_deliv.append(int(input()))

p_store.sort()

ans = 0

for i in p_deliv:
    ok = 0
    ng = n_store
    while ok + 1 < ng:
        mid = int((ok + ng) / 2)
        if p_store[mid] > i:
            ng = mid
        else:
            ok = mid

    ans += min(i - p_store[ok], p_store[ng] - i)

print(ans)
