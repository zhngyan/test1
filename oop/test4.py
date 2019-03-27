#构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次实例化的时候，第一个被自动调用
    #因为主要工作就行初始化，所以得名为构造函数
    def __init__(self):
        print("i am init in dog")

kaka = Dog()

#继承里的构造函数
class Animel():
    pass

class Px(Animel):
    def __init__(self):
        print(" Px—Animel{0}".format(name))

class Dog1():
    def __init__(self):
        print("i am init in dog1")
#实例化的时候，括号的参数需要跟构造函数参数匹配
#自动代用Dog的构造函数
#因为找到了构造函数，则不再查找父类的构造函数
ka1 = Dog1()
#猫没有写构造函数
class Cat (Px):
    pass
#此时应该自动调用构造函数，因为没有，则自动调用父类的构造函数
#在Px中找到了构造方法，则自动调用该构造方法
#c = Cat()
#由于本身没有构造函数，则向上查找，
# 则Px中构造函数中需要两个参数，实例化的时候只给了一个，报错


#继承里的构造函数
class Anime2():
    def __init__(self):
        print("动物")

class Px1(Anime2):
    pass
class Dog2(Px1):
    pass
class Cat1 (Px1):
    pass

ka2 = Dog2()
c = Cat1()

print(type(super))
#help(super)


