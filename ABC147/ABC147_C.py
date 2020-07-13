def honest_people():
    # 入力
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        A.append(int(input()))
        dummy_x = []
        dummy_y = []
        for _ in range(A[i]):
            dummy = []
            dummy = list(map(int, input().split()))
            dummy_x.append(dummy[0])
            dummy_y.append(dummy[1])
        X.append(dummy_x)
        Y.append(dummy_y)
    # 処理
    honest_people_count = set()
    unkind_people_count = set()
    result = []
    for bit in range(1<<N):
        for i in range(N):
            # 正直者の一人を選ぶ
            if bit & (1<<i):
                # 正直者の証言
                for j in range(A[i]):
                    if Y[i][j] == 0:
                        unkind_people_count.add(X[i][j])
                    else:
                        honest_people_count.add(X[i][j])
        for k in range(len(unkind_people_count)):
            if k in honest_people_count:
                return 0
        result.append(len(honest_people_count))
    result.sort(reverse=True)
    return result[0]

result = honest_people()
print(result)
