
'''正则表达式'''

import re


def main1():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    # r的作用是原始字符串的写法，所谓的原始字符串就是表示每个字符都是它原来的意思，更直白一点就是没有转移字符了
    # 因为表示中有很多需要转义的地方，如果使用r，那么\d 就要写成\\d
    u = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    q = re.match(r'^[1-9]\d{4,11}$', qq)
    if not u:
        print('请输入有效的用户名')
    if not q:
        print('请输入有效的QQ号')
    if u and q:
        print('你输入的信息是有效的')

def main2():
    patter = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
       重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
       不是15600998765，也是110或119，王大锤的手机号才是15600998765。
       '''
    mylist = patter.findall( sentence)
    print(mylist)
    print('--------华丽的分割线--------')
    for temp in patter.finditer(sentence):
        print(temp.group())
    print('--------华丽的分割线--------')
    m = patter.search(sentence)
    while m:
        print(m.group())
        m = patter.search(sentence,m.end())

def main3():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    puried = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
    print(puried)
if __name__ == '__main__':
    main3()