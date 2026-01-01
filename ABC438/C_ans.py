import sys

def solve():
    # 入力の高速化
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    # スタックの中身は [数値, 連続数] のリスト
    stack = []
    
    for x in a:
        if stack and stack[-1][0] == x:
            # スタックのトップと同じ数字ならカウントアップ
            stack[-1][1] += 1
            # 4つ揃ったらスタックから消す
            if stack[-1][1] == 4:
                stack.pop()
        else:
            # 違う数字なら新しくスタックに追加
            stack.append([x, 1])
            
    # 最後にスタックに残っている個数を計算
    ans = 0
    for val, count in stack:
        ans += count
        
    print(ans)

solve()