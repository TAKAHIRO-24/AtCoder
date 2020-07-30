def low_elements():
    # 入力
    N = int(input())
    P = list(map(int, input().split()))
    # 初期処理
    count = 0
    # 処理
    for j in range(1, N+1):
        for i in range(j, N+1):
            if P[i-1] <= P[j-1]:
                count += 1
    return count

result = low_elements()
print(result)