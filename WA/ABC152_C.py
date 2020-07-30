def low_elements():
    # 入力
    N = int(input())
    P = list(map(int, input().split()))
    # 初期処理
    # 処理
    for j in range(1, N+1):
        for i in range(j, N+1):
            if not(P[i-1] <= P[j-1]):
                P[i-1] = -1
    # 条件を満たすiの個数
    count = 0
    for num in P:
        if num != -1:
            count += 1
    return count

result = low_elements()
print(result)