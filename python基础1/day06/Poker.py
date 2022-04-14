import random
from enum import Enum, unique
from random import randint

# 使用该注解可以确保一个name只和一个value对应
@unique
class Suite(Enum):
    '''Suite 继承于Enum，是一个枚举类型， 枚举类型中的每个成员属性都是由name和value组成的，'''
    '''枚举类中的属性，其value被分别指定为0,1,2,3'''
    SPADE, HEART, CLUB, DIAMOND = range(4)
    '''魔法函数__lt__主要用于两个实例化的类进行比较，比较的参照物就是在__lt__函数中定义的对象'''
    def __lt__(self, other):
        return self.value < other.value


class Card():
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        suites = ['♠', '♥', '♣', '♦']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    # __repr__方法就是将一个对象用字符串表示出来
    def __repr__(self):
        return self.show()



class Poker():
    def __init__(self):
        self.index = 0
        # 因为Suite是枚举类，通过for suite in  Suite这个语句可以遍历这个枚举类中的各个name的value
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
    def shufle(self):
        random.shuffle(self.cards)
        self.index = 0
    def giver(self):
        card = self.cards[self.index]
        self.index += 1
        return card
    # 查看是否由多余的扑克牌
    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    def __init__(self, name):
        self._name = name
        self.cards =[]
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    def get_one(self,card):
        self.cards.append(card)
    def sort(self, comp = lambda card: (card.suite, card.face)):
        self.cards.sort(key=comp)

def main():
    poker = Poker()
    poker.shufle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.giver())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)

if __name__ == '__main__':
    main()