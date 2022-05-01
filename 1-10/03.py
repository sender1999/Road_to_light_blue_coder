# 問題:AtCoder Beginner Contest 122 B - ATCoder
# 問題URL:https://atcoder.jp/contests/abc122/tasks/abc122_b
# 解法URL:https://atcoder.jp/contests/abc122/submissions/31066436

s = input()

ans = 0

for i in range(len(s)):
    if s[i] in ['A', 'C', 'G', 'T']:
        tmp = 1
        for j in range(i+1, len(s)):
            if s[j] in ['A', 'C', 'G', 'T']:
                tmp += 1
            else:
                break
        ans = max(ans, tmp)

print(ans)
