def achieve_the_goal():
    # 入力
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    # N-1 科目の合計点数
    sum_score = sum(A)
    # N 科目目の最低点数
    x = N*M - sum_score
    # N科目目の最低点数が条件を満たすか
    if x <= 0:
        return 0
    elif x <= K:
        return x
    else:
        return '-1'

result = achieve_the_goal()
print(result)