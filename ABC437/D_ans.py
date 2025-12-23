import sys
from bisect import bisect_left

"""
解き方のポイント
Bj <= Ai : (Ai - Bj)
Bj > Ai : (Bj - Ai) とすれば
sigma(Ai - Bj) = (k * Ai) - (B1 + B2 + ... + Bk)
sigma(Bj - Ai) = (B(k+1) + B(k+2) + ... + Bm) - ((m - k) * Ai) と書ける
"""

def solve():
    # 入力の高速化
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    a = list(map(int, input_data[2:2+n]))
    b = list(map(int, input_data[2+n:2+n+m]))
    
    MOD = 998244353
    
    # 配列Bをソート
    b.sort()
    
    # Bの累積和を計算しておく (0番目を0とした長さM+1のリスト)
    # b_sum[i] = b[0] + b[1] + ... + b[i-1]
    b_sum = [0] * (m + 1)
    for i in range(m):
        b_sum[i+1] = b_sum[i] + b[i]
        
    total = 0
    
    # 各 Ai に対して、Bとの差の合計を計算
    for x in a:
        # x が B のどの位置に入るか（x以下の要素がいくつあるか）を二分探索
        k = bisect_left(b, x)
        
        # 1. B[j] <= x の範囲: (x - B[j]) の合計
        # 合計 = (k * x) - (B[0] + ... + B[k-1])
        low_side = (k * x) - b_sum[k]
        
        # 2. B[j] > x の範囲: (B[j] - x) の合計
        # 合計 = (B[k] + ... + B[m-1]) - ((m - k) * x)
        high_side = (b_sum[m] - b_sum[k]) - ((m - k) * x)
        
        total += low_side + high_side
    
    # 最後に一気にMODを取る
    print(total % MOD)

if __name__ == '__main__':
    solve()