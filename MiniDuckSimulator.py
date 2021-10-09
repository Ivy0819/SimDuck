'''
Author: your name
Date: 2021-10-09 12:32:07
LastEditTime: 2021-10-09 17:44:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\MiniDuckSimulator.py
'''

from FlyClass import *
from QuackClass import *
from DuckClass import *

def main():
    duck1 = DecoyDuck()
    duck1.display()
    duck1.performFly()
    duck1.performQuack()
    duck1.swim()

    duck2 = MallardDuck()
    duck2.display()
    duck2.performFly()
    duck2.performQuack()
    QuackChange = Squeak()
    duck2.setQuackBehavior(QuackChange)#修改叫的方式
    duck2.performQuack()

    duck3 = ModelDuck()
    duck3.display()
    duck3.performFly()
    duck3.performQuack()
    FlyChange = FLyRocketPowered()
    duck3.setFlyBehavior(FlyChange)#修改飞行方式
    duck3.performFly()

    duck4 = ReadHeadDuck()
    duck4.display()
    duck4.performFly()
    duck4.performQuack()

    duck5 = RubberDuck()
    duck5.display()
    duck5.performFly()
    duck5.performQuack()




if __name__ == '__main__':
    main()

