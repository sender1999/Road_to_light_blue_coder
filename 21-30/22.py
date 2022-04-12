# 問題:AtCoder Regular Contest 054 B - ムーアの法則
# 問題URL:https://atcoder.jp/contests/arc054/tasks/arc054_b
# 解法URL:https://atcoder.jp/contests/arc054/submissions/30927096

p = float(input())


def f(x):
    return x + p / (2 ** (x / 1.5))


low = 0
high = 100

for _ in range(500):
    low_2 = f((low * 2 + high) / 3)
    high_2 = f((low + high * 2) / 3)
    if low_2 > high_2:
        low = (low * 2 + high) / 3
    else:
        high = (low + high * 2) / 3

print(f(low))
