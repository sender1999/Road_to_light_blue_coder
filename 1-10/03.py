# 問題:パ研杯2019 C - カラオケ
# 問題URL:https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
# 解法URL:https://atcoder.jp/contests/pakencamp-2019-day3/submissions/30785028

N, M = map(int, input().split())
student_point = []
for i in range(N):
    student_point.append(list(map(int, input().split())))

max_point = -1

for i in range(M - 1):
    for j in range(i, M):
        tmp = 0
        for k in range(N):
            tmp += max(student_point[k-1][i-1], student_point[k-1][j-1])

        max_point = max(max_point, tmp)

print(max_point)
