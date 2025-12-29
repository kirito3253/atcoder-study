from collections import Counter

def solve():
    # 入力を受け取る
    w = input()
    
    # 各文字の出現回数をカウント
    counts = Counter(w)
    
    # すべての出現回数が偶数かどうかをチェック
    for char in counts:
        if counts[char] % 2 != 0:
            print("No")
            return
            
    # 全て偶数ならYes
    print("Yes")

solve()