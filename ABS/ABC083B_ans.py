def solve():
    # 入力を取得
    n, a, b = map(int, input().split())
    
    total = 0
    for i in range(1, n + 1):
        # 数値を文字列に変換し、各桁の数字を合計する
        digit_sum = sum(int(digit) for digit in str(i))
        
        # 判定（Python特有の比較演算子の連結を利用）
        if a <= digit_sum <= b:
            total += i

    print(total)

if __name__ == "__main__":
    solve()