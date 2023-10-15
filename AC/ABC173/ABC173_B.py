def judge_status_summary():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]
    # 判別処理 
    # リスト初期化
    result_list = ['AC', 'WA', 'TLE', 'RE']
    count_list = [0, 0, 0, 0]
    # 集計
    for i in range(N):
        one_count_up_inxex = result_list.index(S[i])
        count_list[one_count_up_inxex] += 1
    # 表示
    for i in range(4):
        print(result_list[i], 'x', count_list[i])

judge_status_summary()