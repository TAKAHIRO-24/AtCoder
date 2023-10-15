def forbidden_list():
    # 入力
    X, N = map(int, input().split())
    P = list(map(int, input().split()))
    # 初期処理
    min_abs_list = list()
    # N = 0 の場合
    if N == 0:
        return X
    # X + i
    i = 0
    while True:
        if X + i in P:
            i += 1
        else:
            min_abs_list.append(X + i)
            break
    # X - i
    i = 0
    while True:
        if X + i in P:
            i -= 1
        else:
            min_abs_list.append(X + i)
            break
    # X との絶対値が最小のもの
    if abs(X - min_abs_list[0]) > abs(X - min_abs_list[1]):
        return min_abs_list[1]
    elif abs(X - min_abs_list[0]) == abs(X - min_abs_list[1]):
        return min(min_abs_list)
    elif abs(X - min_abs_list[0]) < abs(X - min_abs_list[1]):
        return min_abs_list[0]

result = forbidden_list()
print(result)