# 問題:三井住友信託銀行プログラミングコンテスト 2019 D - Lucky PIN
# 問題URL:https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
# 解法URL:https://atcoder.jp/contests/sumitrust2019/submissions/31067866

# Python3だとTLEする。

n = int(input())
s = input()

pass_list = [0] * 1000

for i in range(1000):
    tmp_1 = i % 10
    tmp_10 = (i // 10) % 10
    tmp_100 = i // 100
    flag_1 = True
    flag_10 = True
    flag_100 = True
    for j in range(len(s)):
        if flag_100:
            if int(s[j]) == tmp_100:
                flag_100 = False
                continue
            else:
                continue
        if flag_10:
            if int(s[j]) == tmp_10:
                flag_10 = False
                continue
            else:
                continue
        if flag_1:
            if int(s[j]) == tmp_1:
                flag_1 = False
                pass_list[i] = 1
            else:
                continue

print(sum(pass_list))
