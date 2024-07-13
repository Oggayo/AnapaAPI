import numpy as np


class Neuron:
    def __init__(self, nIn, nN):
        self.w = np.random.rand(nN, nIn) - 0.5
        self.b = np.random.rand(nN, 1) - 0.5
        print("w=", self.w)
        print("b=", self.b)

        self.activation_F = lambda x: (x >= 0).astype(int)

    def train(self, x, t):
        xt = x.T
        e = np.ones(4)

        while e.any():
            i = 0
            for j in xt:
                y = n.query(j)
                e[i] = y - t[i]

                if e[i] < 0:
                     self.w = self.w + j
                    self.b = self.b + 1

                elif e[i] > 0:
                    self.w = self.w - j
                    self.b = self.b - 1
                i = i + 1

    def query(self, inputs):
        s = np.dot(self.w, inputs) + self.b
        return self.activation_F(s)


x = np.array([[0.2, 0.2], [0.2, 1], [1, 0.2], [1, 1]]).T
t = np.array([1, 1, 1, 0])

n = Neuron(2, 1)
n.train(x, t)

x1 = np.array([[1, 0], [0, 1], [1, 0], [1, 1]]).T
print(x1)
print("y=", n.query(x1))
