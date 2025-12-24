import sys

def solve():
    # 入力の受け取り
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    # 嫌いな数字をセットとして持つ（検索を高速化）
    unlike_nums = set(input_data[2:])

    # nから順番に1ずつ増やしてチェック
    x = n
    while True:
        # 数値xを文字列にして、各桁に嫌いな数字が含まれていないか確認
        str_x = str(x)
        is_ok = True
        
        for digit in str_x:
            if digit in unlike_nums:
                is_ok = False
                break
        
        # 嫌いな数字が一つも含まれていなければ、それが答え
        if is_ok:
            print(x)
            break
        
        # 条件を満たさなければ次の数へ
        x += 1

solve()