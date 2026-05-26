class Tensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"

    def mul(self, other):
        self.x *= other.x
        self.y *= other.y

        return self


vector1 = Tensor(5, 2)
vector2 = Tensor(2, 5)
vector3 = vector1.mul(vector2)

print(vector1)
print(vector2)
print(vector3)
