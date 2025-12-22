def find_bill_combination_fast(n, y):
    # 金額が1000で割り切れない場合は即座に終了
    if y % 1000 != 0:
        return -1, -1, -1
    
    y_unit = y // 1000  # 1000円単位で考える
    
    # 10,000円札の枚数だけをループ (O(N)の計算量)
    for i in range(n + 1):
        # 5,000円札の枚数 j を直接計算する式
        # 4j = y_unit - n - 9i より
        numerator = y_unit - n - 9 * i
        
        # 分子が0以上かつ4で割り切れる場合、jが定まる
        if numerator >= 0 and numerator % 4 == 0:
            j = numerator // 4
            k = n - i - j
            
            # 枚数の整合性チェック (jとkが負にならず、合計がnであること)
            if j >= 0 and k >= 0 and i + j + k == n:
                return i, j, k
                
    return -1, -1, -1

n, y = map(int, input().split())
print(*find_bill_combination_fast(n, y))