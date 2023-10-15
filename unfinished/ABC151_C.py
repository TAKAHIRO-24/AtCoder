def welcome_to_atcoder():
    # 入力
    N, M = map(int, input().split())
    p = list()
    S = list()
    for _ in range(M):
        dummy1, dummy2 = input().split()
        p.append(int(dummy1))
        S.append(dummy2)
    # 初期処理
    penalty = 0
    # 処理
    for i in range(M):
        if S[i] == 'WA':
            penalty += 1
        elif S[i] == 'AC':
            


result = welcome_to_atcoder()
