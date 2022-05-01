# 問題:Square869120Contest #6 B - AtCoder Markets
# 問題URL:https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
# 解法URL:

n = int(input())
start_list = []
end_list = []

for _ in range(n):
    a, b = map(int, input().split())
    start_list.append(a)
    end_list.append(b)

start = sum(start_list) // len(start_list)
end = sum(end_list) // len(end_list)

ans = 0

for i in range(n):
    ans += abs(start_list[i] - start)
    ans += abs(start_list[i] - end_list[i])
    ans += abs(end - end_list[i])

print(ans)
