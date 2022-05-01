# 問題:AtCoder Beginner Contest 095 C - Half and Half
# 問題URL:https://atcoder.jp/contests/abc095/tasks/arc096_a
# 解法URL:https://atcoder.jp/contests/abc095/submissions/31066976

a, b, c, x, y = map(int, input().split())

ans = 0

if (a+b)/2 > c:
    ans += min(x, y) * 2 * c
    tmp = min(x, y)
    x -= tmp
    y -= tmp

if a > c*2:
    ans += max(x, 0) * 2 * c
    tmp = max(x, 0)
    x -= tmp
    y -= tmp
else:
    ans += x * a
    x -= x

if b > c*2:
    ans += max(y, 0) * 2 * c
    tmp = max(x, 0)
    x -= tmp
    y -= tmp
else:
    ans += y * b
    y -= y

print(ans)
