import time
def main1():
    try:
        f = open('wenben.txt', 'r', encoding = 'UTF-8')
        print(f.read())
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

def main2():

    with open('wenben.txt', 'r', encoding = 'UTF-8') as f:
        print(f.read())
    print()
    # 按行读取

    with open('wenben.txt', 'r', encoding = 'UTF-8') as f:
        for line in f:
            print(line, end = '')
        print()

    # 按行读取到一个容器之中
    with open('wenben.txt', 'r', encoding = 'UTF-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main2()