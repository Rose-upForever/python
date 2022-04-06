from math import  sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        #直接移动到指定的位置
        self._x = x
        self._y = y

    def increase(self, dx, dy):
        #通过指定的增量进行移动
        self._x += dx
        self._y += dy

    def distance(self, other):
        #计算两个点之间的距离
        dx = self._x - other._x
        dy = self._y - other._y
        return  sqrt(dx ** 2 + dy ** 2)
    # 类似__xx__的方法被称为魔术方法，该类方法可以不被调用，在类被创建的时候可以自动执行

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))


def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_to(5,7)
    print(p2)
    p1.increase(2,3)
    print(p1)
    print(p1.distance(p2))


if __name__ == '__main__':
    main()