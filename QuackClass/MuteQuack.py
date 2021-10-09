'''
Author: your name
Date: 2021-10-08 21:17:27
LastEditTime: 2021-10-09 16:44:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\MuteQuack.py
'''
from QuackClass.QuackBehavior import QuackBehavior
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")