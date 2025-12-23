import sys

"""
解き方のポイント
ソリを引くトナカイの力の合計 >= ソリに乗るトナカイの重さの合計
全トナカイの力の合計 - ソリに乗るトナカイの力の合計 >= ソリに乗るトナカイの重さの合計
全トナカイの力の合計 >= ソリに乗るトナカイの重さ + 力 の合計
"""

def solve():
    # 全ての入力を一度に読み込んで分割する（高速化のコツ）
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr]) # テストケース数
    ptr += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[ptr]) # トナカイの数
        ptr += 1
        
        total_p = 0
        wp_list = []
        
        for _ in range(n):
            w = int(input_data[ptr])
            p = int(input_data[ptr + 1])
            ptr += 2
            
            total_p += p          # 全力の合計を計算
            wp_list.append(w + p) # 「重さ+力」をリストに入れる
        
        # 「重さ+力」が小さい順に並べる
        wp_list.sort()
        
        ans = 0
        current_wp_sum = 0
        for val in wp_list:
            # 累積の(W+P)が全力を超えない限り、ソリに乗せられる
            if current_wp_sum + val <= total_p:
                current_wp_sum += val
                ans += 1
            else:
                break
        results.append(str(ans))
    
    # まとめて出力
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()