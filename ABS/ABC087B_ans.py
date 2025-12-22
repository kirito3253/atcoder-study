import itertools

# 入力値を取得
a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
target_amount = int(input())

# 硬貨の枚数範囲をリスト化
ranges = [
    range(a_500 + 1), 
    range(b_100 + 1), 
    range(c_50 + 1)
]

# すべての組み合わせを生成し、条件に合うものをカウント
count = sum(
    500 * i + 100 * j + 50 * k == target_amount
    for i, j, k in itertools.product(*ranges)
)

print(count)