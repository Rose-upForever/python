class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    #访问器，定义了一个getter方法，可以用于dui属性的访问
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    #修改器，定义了一个setter方法，可以用于dui属性的修改
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
       if self._age <= 16:
           print('%s正在玩飞行棋.' % self._name)
       else:
           print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    #getter方法
    print(person.name)
    person.play()
    #setter方法
    person.name = '白元芳'
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()