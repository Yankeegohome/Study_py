class Person:
    def __init__(self):
        self.name = "bob"


class Square:
    
    square_list = []

    def __init__(self, side):
        self.side = side
        self.P = 0
        self.square_list.append(side)
        print(self.side, (f"на {self.side} "*3))
        pass

    def find_p(self):
        self.P = self.side*4
        print(f"Периметр квадрата = {self.P}")


def tr_or_fl(x, y):
    return x is y


square1 = Square(4)
square2 = Square(6)
square3 = square2
square4 = Square(10).find_p()
square5 = Square(9).find_p()

print(tr_or_fl(square2, square3))









