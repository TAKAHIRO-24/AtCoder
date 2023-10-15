def switch_combination_of_light_on():
    # 入力
    N, M = map(int, input().split())
    K = list()
    S = list()
    for _ in range(M):
        dummy = list(map(int, input().split()))
        K = dummy.pop(0)
        S.append(dummy)
    P = list(map(int, input().split()))
    # 組み合わせ処理
    result = 0
    for bit in range(1 << N):
        right_on = False
        for i in range(M):
            count = 0
            for j in S[i]:
                if bit & (1 << j - 1):
                    count += 1
            if count % 2 == P[i]:
                right_on = True
            else:
                right_on = False
                break
        if right_on:
            result += 1
    # 出力
    print(result)
 
switch_combination_of_light_on()