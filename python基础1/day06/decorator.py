def a_decorator(a_func):
    def embedded():
        print("内嵌函数")
        a_func()
        print("执行过了输入的函数")
    return embedded()

def b_decorator():
    print("我是被输入的函数")

b_decorator = a_decorator(b_decorator);
b_decorator()