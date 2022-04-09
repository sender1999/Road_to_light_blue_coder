# 問題:全国統一プログラミング王決定戦本戦 A - Abundant Resources
# 問題URL:https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a
# 解法URL:https://atcoder.jp/contests/nikkei2019-final/submissions/30801148

N = int(input())
A = list(map(int, input().split()))

s = [0]

for i in range(1, N+1):
    s.append(s[i-1] + A[i-1])

for i in range(1, N+1):
    ans = 0
    for j in range(N+1-i):
        ans = max(ans, s[j+i] - s[j])
    print(ans)
