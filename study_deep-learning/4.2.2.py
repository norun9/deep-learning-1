# 交差エントロピー誤差

import numpy as np


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


# 正解のインデックスでy配列にアクセスし、その位置の数の対数を取る(教科書にこの方法記載)
def cross_entropy_error2(y, t):
    correct_index = np.argmax(t)
    return -np.log(y[correct_index])


t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])

print(cross_entropy_error(y, t), cross_entropy_error2(y, t))
