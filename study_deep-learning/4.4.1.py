import numpy as np


# pythonで数値的に実装する場合、定義の式のままで実装するとプラス側の向きの傾きに偏ってしまいます。
# そこでバランスを取るためにここでは下の式へ修正します。
def numerical_diff(f, x):
    h = 1e-4  # 微小幅hとして十分小さい数値を入れる
    return (f(x + h) - f(x - h)) / 2 * h


# 偏微分関数
def numeral_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    # print(grad)
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)の計算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad


# 勾配法の数式：x = x - q*偏微分 (q=学習率)
def gradient_decent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numeral_gradient(f, x)
        x -= lr * grad

    return x


def function_2(x):
    return x[0] ** 2 + x[1] ** 2


init_x = np.array([-3.0, 4.0])

print(gradient_decent(function_2, init_x=init_x, lr=0.1, step_num=100))
