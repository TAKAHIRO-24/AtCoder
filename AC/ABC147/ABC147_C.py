# def honest_people():
#     # 入力
#     N = int(input())
#     A = []
#     X = []
#     Y = []
#     for i in range(N):
#         A.append(int(input()))
#         dummy_x = []
#         dummy_y = []
#         for _ in range(A[i]):
#             dummy = []
#             dummy = list(map(int, input().split()))
#             dummy_x.append(dummy[0])
#             dummy_y.append(dummy[1])
#         X.append(dummy_x)
#         Y.append(dummy_y)
#     # 処理
#     honest_people_count = set()
#     unkind_people_count = set()
#     result = []
#     for bit in range(1<<N):
#         for i in range(N):
#             # 正直者の一人を選ぶ
#             if bit & (1<<i):
#                 # 正直者の証言
#                 for j in range(A[i]):
#                     if Y[i][j] == 0:
#                         unkind_people_count.add(X[i][j])
#                     else:
#                         honest_people_count.add(X[i][j])
#         for k in range(len(unkind_people_count)):
#             if k in honest_people_count:
#                 return 0
#         result.append(len(honest_people_count))
#     result.sort(reverse=True)
#     return result[0]

# result = honest_people()
# print(result)

def honest_or_unkind():
    # 初期化
    A = list()
    x = list()
    y = list()
    # 入力
    N = int(input())
    for i in range(N):
        A.append(int(input()))
        dummy_x = list()
        dummy_y = list()
        for _ in range(A[i]):
            dummy = list(map(int, input().split()))
            dummy_x.append(dummy[0])
            dummy_y.append(dummy[1])
        x.append(dummy_x)
        y.append(dummy_y)
    # 処理
    # bitと証言が矛盾しないか判別するフラグ
    is_contradiction = False
    # 正直者の数
    honest_count = list()
    # 正直者にbitを立てる
    for bit in range(1 << N):
        for i in range(N):
            # i番目の人が正直者かどうか
            if bit & 1 << i:
                # 証言の個数だけループ
                for j in range(A[i]):
                    # x[i][j]が不親切
                    if y[i][j] == 0:
                        # bitと証言が一致
                        str_bit = str(bit).rjust(N)
                        if str_bit[(x[i][j] - 1)] == '0':
                            pass
                        else:
                            is_contradiction = True
                            break
                    # x[i][j]が親切
                    else:
                        # bitと証言が一致
                        str_bit = str(bit).rjust(N)
                        if str_bit[(x[i][j] - 1)] == '1':
                            pass
                        else:
                            is_contradiction = True
                            break
        # 当該bitの組み合わせで正直者とその証言が矛盾しなかった場合
        if not is_contradiction:
            honest_count.append(str(bit).count('1'))
    # 矛盾のない組み合わせの中から正直者が最も多いときの人数を取得
    return max(honest_count)

result = honest_or_unkind()
print(result)