'''
Author: your name
Date: 2021-10-08 20:44:35
LastEditTime: 2021-10-09 17:41:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\Duck.py
'''
class Duck:
    def __init__(self, flyParam, quackparam) -> None:
        print("--------------------------------")
        self.flyBehavior = flyParam
        self.quackBehavior = quackparam
    def setFlyBehavior(self,flyParam):
        print("...Changing Fly Behavior...")
        self.flyBehavior = flyParam
    def setQuackBehavior(self,quackparam):
        print("...Changing Quack Behavior...")
        self.quackBehavior = quackparam
    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()
    def display(self):
        pass
    def swim(self):
        print("All ducks float, even decoys!")


