def quick_sort(items, comp = lambda x, y : x <= y):
    item = list(items)[:]
    _quick_sort(item, 0, len(item) - 1, comp)
    return item


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def partition(items, start, end, comp):
       privot = items[end]
       # i 是指向比枢轴元素小的那一部分数组的最后一个元素，最开始默认为空，所以让其值开始位置左边的那一个位置
       i = start - 1;
       for j in range(start, end):
           # 如果位置j上的元素小于枢轴元素，且i是指向小于枢轴元素的部分的最后一个元素，那么先让i ++，然后交换i和j位置上元素。 算法的具体原理
           # 详见算法导论。
           if comp(items[j], privot):
               i += 1
               items[i], items[j] = items[j], items[i]
       # 更换枢轴元素的位置
       items[i + 1], items[end] = items[end], items[i + 1]
       return i + 1