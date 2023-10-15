"""
1 ----- 2 ----- ai ----- bi -----
                    辺:i
"""
import itertools

def one_stroke_path():
    """
    N : 頂点
    M : 辺数
    ai, bi : 辺iの両端の頂点
    """
    # 入力
    N, M = map(int, input().split())
    a = list()
    b = list()
    for _ in range(M):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)
    
    # 処理
    permutations_list = itertools.permutations([x for x in range(1,N+1)])
    count = 0
    for one_case in permutations_list:
        is_ok = False
        if one_case[0] == 1:
            # 順序を一つずつ取り出す
            for i in range(len(one_case)-1):
                # 道を一つずつ取り出す
                for j in range(M):
                    # 頂点を両端に持つ道を探す
                    if (one_case[i] == a[j] and one_case[i+1] == b[j]) or (one_case[i] == b[j] and one_case[i+1] == a[j] ):
                        # 頂点を両端に持つ道があればbreak
                        is_ok = True
                        break
                    else:
                        # なければほかの道を探す
                        is_ok = False
                # 全ての道の両端に頂点が該当しなければ、そのone_caseはNO
                if is_ok == False:
                    break
        # one_caseの先頭が１以外はNO
        else:
            is_ok = False
        if is_ok:
            count += 1
    return count

result = one_stroke_path()
print(result)

