def multiple_of_nine():
    # 入力
    N = int(input())
    # 処理
    if N / 9 == N // 9:
        # Nの各桁の和
        str_N = str(N)
        each_digit_sum = 0
        for i in range(len(str_N)):
            each_digit_sum += int(str_N[i])
        if each_digit_sum / 9 == each_digit_sum // 9:
            return 'Yes'
        else:
            return 'No'

result = multiple_of_nine()
print(result)