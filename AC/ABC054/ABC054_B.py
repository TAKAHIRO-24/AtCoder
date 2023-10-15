def template_matching():
    # 入力
    N, M = map(int, input().split())
    A = list()
    B = list()
    for _ in range(N):
        dummy = input()
        A.append(dummy)
    for _ in range(M):
        dummy = input()
        B.append(dummy)
    # 比較
    for i in range(M):
        for j in range(N):
            # M*Mの一行目がN*Nのいずれかの列に含まれるか
            if B[i] in A[j]:
                row = A[j].find(B[i])
                line = j
                # 正方形を含むか否か
                for k in range(M):
                    if B[k] == A[line+k][row:row+M]:
                        include = True
                    else:
                        include = False
                        break
                if include:
                    return True
    return False

# 出力
if template_matching():
    print('Yes')
else:
    print('No')