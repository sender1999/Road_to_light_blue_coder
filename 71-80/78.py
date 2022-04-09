# 問題:JOI 2011 本選 1 - 惑星探査
# 問題URL:https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho1
# 解法URL:

# 計算量がN(MN+K)なのはあってるけど、入力がinput()だとTLEする
# sys.stdin.readline()とか使わないと間に合わない多分

M, N = map(int, input().split())
K = int(input())

jan = []
oce = []
ice = []

for i in range(M):
    tmp = input()
    tmp_j = [0]
    tmp_o = [0]
    tmp_i = [0]
    for j in range(len(tmp)):
        if tmp[j] == 'J':
            tmp_j.append(tmp_j[-1]+1)
            tmp_o.append(tmp_o[-1])
            tmp_i.append(tmp_i[-1])
        elif tmp[j] == 'O':
            tmp_j.append(tmp_j[-1])
            tmp_o.append(tmp_o[-1]+1)
            tmp_i.append(tmp_i[-1])
        elif tmp[j] == 'I':
            tmp_j.append(tmp_j[-1])
            tmp_o.append(tmp_o[-1])
            tmp_i.append(tmp_i[-1]+1)

    jan.append(tmp_j)
    oce.append(tmp_o)
    ice.append(tmp_i)

for i in range(K):
    y_s, x_s, y_e, x_e = map(int, input().split())
    ans_j = 0
    ans_o = 0
    ans_i = 0
    for j in range(y_s-1, y_e):
        ans_j += jan[j][x_e] - jan[j][x_s-1]
        ans_o += oce[j][x_e] - oce[j][x_s-1]
        ans_i += ice[j][x_e] - ice[j][x_s-1]

    print('{} {} {}'.format(ans_j, ans_o, ans_i))
