# class 类名(父类名)
class Thing(object):
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def name(self):
        return  self._name
    @property
    def price(self):
        return  self._price

    @property
    def weight(self):
        return self._weight

    @name.setter
    def name(self,name):
        self._name = name

    @price.setter
    def price(self, price):
        self._price = price

    @weight.setter
    def weight(self, weight):
        self._weight = weight
    @property
    def value(self):
        return self._price / self._weight


# 输入物品信息
def input_things():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    maxweight, num = map(int, input().split())
    all_things = []
    for _ in range(num):
        # 类中传入的参数应该和类中所包含的属性相一致
        # all_things中存储的是一个个的物品对象。
        all_things.append(Thing(*input_things()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight, total_value = 0, 0
    for thing in all_things:
        if total_weight + thing.weight <= maxweight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_value += thing.price
    print(f'总价值：{total_value}')
if __name__ == '__main__':
    main()


