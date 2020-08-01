def low_elements():
    # 入力
    N = int(input())
    P = list(map(int, input().split()))
    # 初期処理
    joken_list = [True] * N
    # 処理
    for i in range(N):
        for j in range(0, i):
            if not(P[i] <= P[j]):
                joken_list[i] = False
                break
    # 条件を満たすiの個数
    count = 0
    for joken in joken_list:
        if joken:
            count += 1
    return count

result = low_elements()
print(result)