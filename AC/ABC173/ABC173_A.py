def A_Payment():
    # 入力
    N = int(input())
    # 計算処理
    i = 1
    while True:
        if 1000 * i >= N:
            return 1000 * i - N
        else:
            i += 1

result = A_Payment()
print(result)