'''
Author: your name
Date: 2021-10-09 16:55:16
LastEditTime: 2021-10-09 17:18:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\DuckClass\MallardDuck.py
'''
from DuckClass.Duck import Duck
from FlyClass.FlyWithWings import FlyWithWings
from QuackClass.Quack import Quack

class MallardDuck(Duck):
    def __init__(self, flyParam=FlyWithWings(), quackParam=Quack()) -> None:
        super().__init__(flyParam, quackParam)#集成父类super的init参数不需要self；
    def display(self):
        print("I'm a real Mallard Duck")