'''
Author: your name
Date: 2021-10-08 21:19:38
LastEditTime: 2021-10-09 16:46:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\DecoyDuck.py
'''

from DuckClass.Duck import Duck
from FlyClass.FlyNoWay import FlyNoWay
from QuackClass.MuteQuack import MuteQuack
class DecoyDuck(Duck):
    def __init__(self, flyParam=FlyNoWay(), quackParam=MuteQuack()) -> None:
        super().__init__(flyParam, quackParam)#集成父类super的init参数不需要self；
    def display(self):
        print("I'm a duck Decoy")