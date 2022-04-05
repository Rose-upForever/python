'''
# 测试python中函数默认值功能
from random import randint

def roll_dice(n = 2):
    total = 0
    #_的作用相当于i，但是_不会被具体使用，其只用于表示循环次数
    for _ in range(n):
       total += randint(1, 6)
    return total

def add(a = 0, b = 0, c = 0):
    return a + b + c

print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1,2,3))
print(add(1))
'''

'''
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] =yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
'''


'''
from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
'''



'''
#双色球问题
from random import randrange,random,randint,sample

def random_select():
    red_balls = [x for x in range(1,34)]
    
    # sample的作用是从集合red_balls中随机选6个对象
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls
 
def display(balls):
    #enumerate()是为集合balls生成枚举对象，枚举类型主要由所有和Value组成。
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            # print函数默认打印玩一行之后会换行，end = ‘ ’的作用就是不让其换行，而是输出一个空格
            print('|', end = ' ')
        print('%02d' % ball, end=' ')
    # 该语句的主要作用是换行
    print()

def main():
    n = int(input('选几注：'))
    for _ in range(n):
        display(random_select())
if __name__ == '__main__':
    main()
'''


#约瑟夫环问题
def find_genius():
    persons = [True] * 30 
    counter, index, num = 0,0,0 
    while counter < 15:
        if persons[index]:
            num += 1
        if num == 9:
            persons[index] = False
            num = 0
            counter += 1
        index += 1
        # 保证索引的值一直是从0到29
        index %= 30
    for person in persons:
        if person:
            print("基", end = ' ')
        else:
            print('非',end = ' ')
if __name__ == '__main__':
    find_genius()






































    
    
    