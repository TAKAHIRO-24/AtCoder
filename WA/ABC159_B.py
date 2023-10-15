def judge_palindrome(string):
    """
    文字列を引数に、回文か否かを判別する。
    string：文字列
    return True or False
    """
    # 文字数
    str_count = len(string)
    # 文字列の先頭にダミー文字を挿入
    string = '0' + string
    # 偶数
    if str_count % 2 == 0:
        for i in range(1, (str_count//2)+1):
            if string[i] == string[-i]:
                pass
            else:
                return False
    # 奇数
    if str_count % 2 == 1:
        for i in range(1, (str_count+1)//2):
            if string[i] == string[-i]:
                pass
            else:
                return False
    return True

def string_palindrome():
    # 入力
    S = input()
    # 初期処理
    N = len(S) # 文字列の長さ
    is_palindrome = list() # 条件１，２で回文か否かを保存
    string = list()
    # 条件設定
    string.append(S[0:(N-1)//2]) # 条件１
    string.append(S[(N+3)//2-1:N]) # 条件２
    for i in range(2):
        result = judge_palindrome(string[i])
        is_palindrome.append(result)
    # 戻り値
    if is_palindrome[0] and is_palindrome[1]:
        return 'Yes'
    else:
        return 'No'

result = string_palindrome()
print(result)