class MulLayer:
    def __init__(self) -> None:
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out

    def backward(self, dout):
        # dout:微分に対して、順伝播のひっくり返した値を蒸散して下流に流す
        # xに関する微分は、dout * y
        # yに関する微分は、dout * x
        print("self:", self.x, self.y)
        dx = dout * self.y  # xとyをひっくり返す
        dy = dout * self.x

        return dx, dy


apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

# backward
dprice = 1  # 価格の微分
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax)
