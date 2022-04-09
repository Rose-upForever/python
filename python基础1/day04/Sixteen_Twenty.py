def method()
list1 = ['key1', 'key2', 'key3']
list2 = [1, 2, 3]
# python中的items方法表示以列表的形式返回可遍历的（键值，值）元组

prices2 = {key: value for key in list1 for value in list2}

print(prices2)

