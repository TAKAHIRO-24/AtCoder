# 入力
N = int(input())
L = list(map(int, input().split()))

# 処理
triangle = 0
for bit in range(1<<len(L)):
    count = 0
    dummy = list()
    for i in range(len(L)):
        if bit & (1<<i):
            count += 1
            dummy.append(L[i])
    if count == 3:
        if dummy[0] != dummy[1] != dummy[2]:
            triangle += 1

# 結果
print(triangle)