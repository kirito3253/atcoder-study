import sys

def solve():
    # 入力の読み込み
    H, W, A, B = map(int, sys.stdin.readline().split())
    MOD = 10**9 + 7

    # 階乗とその逆元を前計算しておく (nCrを高速に求めるため)
    MAX = H + W + 1
    fact = [1] * MAX
    inv = [1] * MAX
    for i in range(1, MAX):
        fact[i] = (fact[i-1] * i) % MOD
    
    # フェルマーの小定理を用いて逆元を計算
    inv[MAX-1] = pow(fact[MAX-1], MOD - 2, MOD)
    for i in range(MAX-2, -1, -1):
        inv[i] = (inv[i+1] * (i+1)) % MOD

    def nCr_mod(n, r):
        if r < 0 or r > n:
            return 0
        num = fact[n]
        den = (inv[r] * inv[n-r]) % MOD
        return (num * den) % MOD

    ans = 0
    # 境界となる各列 i について経路を計算
    # スタートから (H-A, i) までの経路 × (H-A+1, i) からゴールまでの経路
    for i in range(B + 1, W + 1):
        # スタート(1,1)から点(H-A, i)までの経路
        path_to_border = nCr_mod((H - A - 1) + (i - 1), i - 1)
        # 点(H-A+1, i)からゴール(H,W)までの経路
        path_from_border = nCr_mod((A - 1) + (W - i), W - i)
        
        ans += (path_to_border * path_from_border) % MOD
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    solve()