# 問題:AtCoder Beginner Contest 106 D - AtCoder Express 2
# 問題URL:https://atcoder.jp/contests/abc106/tasks/abc106_d
# 解法URL:

N, M, Q = map(int, input().split())

s = [0]*(N+1)
for i in range(N+1):
    start, end = map(int, input().split())
    s[start:end+1] = [x+1 for x in s[start:end+1]]

#for i in range(1, N+1):
#    s[i] += s[i-1]

for i in range(Q):
    start, end = map(int, input().split())

print(s)
