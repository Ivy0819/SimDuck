'''
Author: your name
Date: 2021-10-09 16:57:30
LastEditTime: 2021-10-09 17:19:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\DuckClass\ModelDuck.py
'''
from DuckClass.Duck import Duck
from FlyClass.FlyNoWay import FlyNoWay
from QuackClass.Quack import Quack

class ModelDuck(Duck):
    def __init__(self, flyParam=FlyNoWay(), quackParam=Quack()) -> None:
        super().__init__(flyParam, quackParam)#集成父类super的init参数不需要self；
    def display(self):
        print("I'm a model duck")