from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def c(self):
        return self._c
    @a.setter
    def a(self, a):
        self._a = a
    @b.setter
    def b(self, b):
        self._b = b
    @c.setter
    def c(self, c):
        self._c = c
    # 定义静态方法，用以表示类中的方法，而不是对象的方法，不可以通过对象进行调用
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter() / 2
        return (half * (half - self._a) * (half - self._b) * (half - self._c)) ** 0.5

def main():
    a, b, c = 3, 4, 5
    # 静态方法通过类名进行调用
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        #对象方法通过对象进行调用
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形')
if __name__ == '__main__':
    main()
