# 面向对象知识的学习

class Student(object):
    # init函数主要用于在实例化对象的时候调用，用于类中的一些属性进行初始化曹祖
    # 通过这个方法我们可以为创建的对象绑定name，score这两个属性,也就是可以通过self引用这两个对象
    # 属性self指的是将要被创建的实例对象
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 当在一个方法或属性前面加上两个下划线的时候，属性表示私有的，对外不可见
        self.__name = name
    def study(self, course_name):
        # %s的作用是用于格式化输出，%s相当于一个占位符，用于输出%后面的内容
        print('%s is studying %s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s去看熊出没' % self.name)
        else:
            print('%s去看爱情片 ' % self.name)

# 使用创建好的类
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()

# __name__ == '__main__'表示在当前文件中执行以下代码，为了当该模块被导入到其他模块的时候，该语句下的代码不会被执行


if __name__ == '__main__':
    main()