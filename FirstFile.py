from TestFile import TestFile

i = 0



def printFun(s):
    print(str(s))


for i in range(10, 20):
    printFun(i)
# assert i==5,"error occured so what should i do"

test = TestFile(10, 5, "pookie")
test.multyply()
print(test.name)

test.name = "rahul"
print(getattr(test, "name"))
print(hasattr(test, "name"))
print(hasattr(test, "name5"))
delattr(test, "name")
print("after del opration performed " + str(hasattr(test, "name")))

print(type(i))
print(print())
