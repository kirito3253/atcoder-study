# 入力の受け取り
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# 宿泊日数がK日以下の場合
if N <= K:
    ans = N * X
# 宿泊日数がK日を超える場合
else:
    # 最初のK日分 ＋ 残りの(N-K)日分
    ans = K * X + (N - K) * Y

print(ans)