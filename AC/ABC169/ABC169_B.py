def multiplication():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # かける数に0があるか確認
    if 0 in A:
        return 0
    # 計算処理
    multi = 1
    for i in range(N):
        multi = multi * A[i]
        # 10^18比較
        if multi > 10 ** 18:
            return -1
    return multi

result = multiplication()
print(result)