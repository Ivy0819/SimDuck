'''
Author: your name
Date: 2021-10-09 17:22:38
LastEditTime: 2021-10-09 17:29:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\DuckClass\RubberDuck.py
'''
from DuckClass.Duck import Duck
from FlyClass.FlyNoWay import FlyNoWay
from QuackClass.Squeak import Squeak

class RubberDuck(Duck):
    def __init__(self, flyParam=FlyNoWay(), quackParam=Squeak()) -> None:
        super().__init__(flyParam, quackParam)#集成父类super的init参数不需要self；
    def display(self):
        print("I'm a rubber duckie")

