'''
Author: your name
Date: 2021-10-08 20:40:25
LastEditTime: 2021-10-09 16:43:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\FlyNoWay.py
'''
from FlyClass.FlyBehavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self):
        print ("I can't fly")
