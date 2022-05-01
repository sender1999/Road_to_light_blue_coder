# 問題:ITP1_7_B - How Many Ways?
# 問題URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
# 解法URL:https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=6494906#1

while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i+j+k == x:
                    ans += 1
    print(ans)
