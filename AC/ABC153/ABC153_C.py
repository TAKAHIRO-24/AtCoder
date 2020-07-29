def fennec_vs_monster():
    # 入力
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    # 体力リストの大きい順からK個だけ排除
    for i in range(K):
        # 体力リストが空でないときは以下を実行
        if i < N:
            max_H = max(H)
            H.remove(max_H)
    # 残りの体力リストを合計
    sum_H = sum(H)
    # 攻撃の回数の最小値
    return sum_H

result = fennec_vs_monster()
print(result)