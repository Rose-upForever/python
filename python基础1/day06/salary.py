from abc import  ABCMeta, abstractmethod

class Emplyee(metaclass = ABCMeta):
    '''定义雇员抽象类'''
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name


    '''定义一个抽象方法，其具体实现交给子类'''
    @abstractmethod
    def employee_salary(self):
        pass

# 创建经理类
class Manager(Emplyee):
    def employee_salary(self):
        return 15000.0

# 创建程序员类
class Program(Emplyee):
    def __init__(self, name, workhour = 0):
        self._workhour = workhour
        super().__init__(name)
    @property
    def workhour(self):
        return self._workhour

    @workhour.setter
    def workhour(self, workhour):
        self._workhour = workhour

    def employee_salary(self):
        return 200.0 * self._workhour


# 创建售货员类
class Salesman(Emplyee):
    def __init__(self, name, salesnum = 0):
        self._salesnum = salesnum
        super().__init__(name)

    @property
    def salesnum(self):
        return  self._salesnum

    @salesnum.setter
    def salesnum(self, salesnum):
        self._salesnum = salesnum

    def employee_salary(self):
        return 1800.0 + self.salesnum * 0.05


# 创建员工的工程仓  ---工厂模式（通过工厂实现对象使用者和对象之间的解耦合）
class EmplyeeFactory:
    @staticmethod
    def create(em_type, *args, **kwargs):
        all_em_types = {'M': Manager, 'P': Program, 'S': Salesman}
        # 将对应的类名赋值给cls变量， 然后在return中调用类的构造方法
        cls = all_em_types[em_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    emps=[
        EmplyeeFactory.create('M', '曹操'),
        EmplyeeFactory.create('P', '郭嘉', 85),
        EmplyeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}:{emp.employee_salary()}')


if __name__ == '__main__':
    main()
