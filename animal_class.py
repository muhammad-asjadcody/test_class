from abc import ABC, abstractclassmethod

class Animal(ABC):

    def move(self):
        pass
class human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):

    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark and fetch")

class lion(Animal):
    def move(self):
        print("i can roar and hunt")

R = human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = lion()
K.move()

