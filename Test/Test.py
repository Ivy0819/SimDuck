'''
Author: your name
Date: 2021-10-09 14:55:32
LastEditTime: 2021-10-09 15:04:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \week4\Test.py
'''

class QuackBehavior:
    def quack(self):
        '''
        accomplish quack function
        '''

class FakeQuack(QuackBehavior):
    def quack(self):
        print("qwak")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class Quack(QuackBehavior):
        def quack(self):
            print("Quack")

class FlyBehavior:
    def fly(self):
        '''
        accomplish fly function here
        '''
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with wings!")

class FLyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print ("I can't fly")

class Duck:
    def __init__(self, flyParam, quackparam) -> None:
        self.flyBehavior = flyParam
        self.quackBehavior = quackparam
    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()
    def display(self):
        pass
    def swim(self):
        print("All ducks float, even decoys!")

class DecoyDuck(Duck):
    def __init__(self, flyParam=FlyNoWay(), quackParam=MuteQuack()) -> None:
        print("-----------------------------")
        super().__init__(flyParam, quackParam)#集成父类super的init参数不需要self；
    def display(self):
        print("I'm a duck Decoy")
        

def main():
    duck1 = DecoyDuck()
    duck1.display()
    duck1.performFly()
    duck1.performQuack()

if __name__ == '__main__':
    main()
