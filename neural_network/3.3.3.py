import numpy as np

# 行列の積

# x = np.array([1, 2])
# w = np.array([[1, 3, 5], [2, 4, 6]])
# print(np.dot(x, w))

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)
print(a)
b = np.array([[4, 5], [5, 6]])
print(b)
# shape is 3 * 2
print(np.dot(a, b))
