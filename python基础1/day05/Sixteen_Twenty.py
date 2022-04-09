import heapq

list1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
# lambda用于创建小型匿名函数，如x = lambda a : a+10 就是将发送的任意数字加10
# heaqp的key指定了一个单参数函数，用于从iterable中提取比较键
print(heapq.nsmallest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))