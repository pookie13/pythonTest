from Abc import Abcd
from ParentFile import ParentFile
from TestFile1 import TestFile1


class TestFile(ParentFile, TestFile1):
    hight = 0
    width = 0
    name = 1

    def __init__(self, h, w, name):
        #  print("counstructer called")
        self.hight = h
        self.width = w
        self.name = name
        ''' print("hight" + str(self.hight))
 print("width" + str(self.width))
 print("name" + str(self.name))'''

    def multyply(self):
        if self.__module__ == '__multyply__':
            print(self.hight * self.width)
        else:
            print("else case in TestFile")


if TestFile.__module__ == '__main__':
    print(TestFile.multyply())



print("Super Class Function Call" + str(ParentFile.addFunction(10, 5)))
# t1 = TestFile1()
print("devide by value" + str(TestFile1.devide(10, 2)))

abc = Abcd()

print("Minus by value" + str(abc.minus(10, 2)))
