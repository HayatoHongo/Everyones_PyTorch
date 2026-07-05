class MyLinear:
    def __init__(self, weight=0.0):
        self.weight = weight

    def forward(self, x):
        return self.weight * x


MyMyLinear = MyLinear
