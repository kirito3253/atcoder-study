import sys

def solve():
    # 入力を受け取る
    s = input().strip()
    
    # ターゲットとなる単語をすべて反転させる
    # dream   -> maerd
    # dreamer -> remaerd
    # erase   -> esare
    # eraser  -> resare
    words = ["dream", "dreamer", "erase", "eraser"]
    rev_words = [w[::-1] for w in words]
    
    # 元の文字列も反転させる
    s_rev = s[::-1]
    
    i = 0
    can_make = True
    
    # 文字列の端から順番にチェックしていく
    while i < len(s_rev):
        matched = False
        for word in rev_words:
            # 現在の地点から単語が一致するか確認
            if s_rev[i:i+len(word)] == word:
                i += len(word)
                matched = True
                break
        
        # どの単語とも一致しなかった場合は作成不可能
        if not matched:
            can_make = False
            break
            
    if can_make:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()