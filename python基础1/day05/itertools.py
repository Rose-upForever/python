import itertools
from collections import Counter
# itertools是操作迭代器的一个工具集合。
# 产生ABCD的全排列
def main1():
    itertools.permutations('ABCD')
    # 产生ABCDE的五选三组合
    itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    itertools.product('ABCD', '123')
    # 产生ABC的无限循环序列
    itertools.cycle(('A', 'B', 'C'))
def main2():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    # 统计单词出现的次数
    counter = Counter(words)
    print(counter.most_common(3))


# 简单选择排序
def select_sort(items,  comp = lambda x, y: x < y):
    # 列表[:]实际上是创建列表的一个副本，这样对于列表的操作将不会影响到原来的列表。
    item = items[:]
    for i in range(len(item) - 1):
        min_index = i
        for j in range(i + 1, len(item)):
            if comp(item[j], item[min_index]):
                min_index = j
        item[i], item[min_index] = item[min_index], item[i]
    return item


# 冒泡排序
def bubble_sort(items, comp = lambda x, y : x > y):
    item = items[:]
    for i in range(len(item) - 1):
        swap = False
        for j in range(len(item) - 1 - i):
            if comp(item[j], item[j + 1]):
                item[j], item[j + 1] = item[j + 1], item[j]
                swap = True
        # 如果一轮下来，各个元素之间都没有发生一次交换，也就是说元素之间已经有序了，所以排序完成，跳出循环
        if not swap:
            break
    return item


# 鸡尾酒排序(搅拌排序)
def Cocktail_sort(items, comp = lambda x, y : x < y):
    item = items[:]
    for i in range(len(item) - 1):
        swap = False
        for j in range(len(item) - i - 1):
            if comp(item[j + 1], item[j]):
                swag = True
                item[j + 1], item[j] = item[j], item[j + 1]

        if swap:
            swap = False

            '''range 函数中参数的用法
            range(start, end, start)
            range(start, end)
            range(end)
            '''
            for j in range(len(item) - 2 - i, i, -1):
                if comp(item[j], item[j + 1]):
                    swap = True
                    item[j + 1], item[j] = item[j], item[j + 1]
        if not swap:
            break
        return item

def merge(items1, items2, comp = lambda x, y : x < y):
    item1 = items1[:]
    item2 = items2[:]
    items = []
    index1, index2 = 0, 0
    while index1 < len(item1) and index2 < len(item2):
        if comp(item1[index1], item2[index2]):
            items.append(item1[index1])
            index1 += 1
        else:
            items.append(item2[index2])
            index2 += 1
    # 加上列表中剩余的数据
    items += item1[index1:]
    items += item2[index2:]

# 归并排序
def merge_sorted(items, comp = lambda x, y : x < y):
    item = items[:]
    if len(item) < 2:
        return  item
    mid = len(item) // 2
    left = merge_sorted(item[:mid],comp)
    right = merge_sorted(item[mid:],comp)
    return merge(left, right, comp)

if __name__ == '__main__':
    main2()