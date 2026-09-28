from abc import ABC, abstractclassmethod

class ABsclass(ABC):

    def print(self,x):
        print("passed value is", x )


    @abstractclassmethod
    def task(self):
        print("we are inside of the abcclass")

class test_class(ABsclass):
    def task(self):
        print("we are inside of the test class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)
