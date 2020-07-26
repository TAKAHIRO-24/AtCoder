def peak():
    # 入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = list()
    B = list()
    for _ in range(M):
        dummy = list(map(int, input().split()))
        A.append(dummy[0])
        B.append(dummy[1])
    # 初期処理
    is_good_list = list()
    # 各展望台が良い展望台か判別
    for ovservatory_num in range(1,N+1):
        is_good = True # 良い展望台 = True, 悪い展望台 = False
        for j in range(M):
            if A[j] == ovservatory_num:
                if H[A[j] - 1] > H[B[j] - 1]:
                    is_good = True
                else:
                    is_good = False
                    break
            elif B[j] == ovservatory_num:
                if H[B[j] - 1] > H[A[j] - 1]:
                    is_good = True
                else:
                    is_good = False
                    break
            else:
                pass
        is_good_list.append(is_good)
    # 良い展望台の個数
    return is_good_list.count(True)    

result = peak()
print(result)