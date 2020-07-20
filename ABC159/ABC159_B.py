def string_palindrome():
    # 入力
    S = input()
    # 初期処理
    N = len(S)
    condition1 = int((N-1)/2)
    condition2 = int((N+3)/2)
    # 回文判定
    # 条件1
    cond1_string1 = S[0:condition1]
    cond1_string2 = '0'+cond1_string1
    stop = int((len(cond1_string1)-1/2)+1)
    for i in range(1,stop):
        if cond1_string2[i] == cond1_string2[-i]:
            pass
        else:
            return 'No'
    # 条件2
    cond2_string1 = S[-1:condition2-1]
    cond2_string2 = '0'+cond2_string1
    stop = int((len(cond2_string1)-1/2)+1)
    for i in range(1,stop):
        if cond2_string2[i] == cond2_string2[-i]:
            pass
        else:
            return 'No'
    # 条件1，2をクリア
    return 'Yes'

result = string_palindrome()
print(result)