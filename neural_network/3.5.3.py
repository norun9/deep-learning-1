import numpy as np


def softmax(a):
    max = np.max(a)
    exp_a = np.exp(a - max)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([1010, 1000, 990])
y = softmax(a)
# ソフトマックス関数の出力は0から1.0の間の実数になる
# また、ソフトマックス関数の出力の総和は1になる
print(np.sum(y))
