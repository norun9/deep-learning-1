import numpy as np


# 二乗和誤差
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# ラベル2を正解(1)とする
t = [0, 0, 1, 0, 0, 0, 0, 0, 0]

# 一番高いのはラベル1
y = [0.6, 0.05, 0.0, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0]

# 値が小さいほど誤差が少ない
# 二乗和誤差が大きいと、予測値が実際の値からかけ離れていることを示しています。
print(mean_squared_error(np.array(y), np.array(t)))
