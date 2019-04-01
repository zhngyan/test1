#属性案例
#创建Student类，描述学生类，类中有name属性，但name格式并不统一
#可以用增加一个函数，自动调用的方式，但很蠢
class Stundet():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name) #修改name属性变为大写
    def intro(self):
        print("hello, my name is {0}".format(self.name))
    def setName(self, name):
        self.name = name.upper()
s1 = Stundet("Yan Zhang",24)
s2 = Stundet("GZY",24)
s1.intro()
s2.intro()

#property案例
#定义一个Person类，具有name，age属性，对任意输入姓名，使用大写保存，年龄用整数保存
class Person():
    '''
    说明文档属性解释
    name ： 姓名
    age ： 年龄
    '''
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        #被注释代码会引起死循环，此种情况，为避免规定统一调用父类魔法函数
        #self.name = value
        super().__setattr__(name, value)
    def fget(self):
        return  self._name
    def fset(self, name):
        #所有输入的姓名用大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"

    name = property(fget ,fset,fdel)

p1 = Person()
p1.name = "Zhang Yan"
print(p1.name)
print(p1.__dict__)
# 死循环调动
p1.age =18

#类的内置属性
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)

#__call_str 举例
class A():
     def __init__(self,name = 0 ):
         print("hha")
     def __call__(self):
         print("哈哈")
     def __str__(self):
         return "HAHHA"
     def __getattr__(self, name):
         print("No Find")
         print(name)

a = A()
a()
print(a)
print(a.name)
print(a.addr)
print("*"*80)
class B():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print('哈哈,{0}会比{1}大？'.format(self, obj))
        return self._name > obj._name
b1 = B("1")
b2 = B("2")
print(b1 > b2)

#三种方法的案例
class C():
    def eat(self):
        print(self)
        print("eat")

    #类方法
    @classmethod
    def play(cls):
        print(cls)
        print("play")

    #静态方法
    @staticmethod
    def say():
        print("say")
#实例方法
zy = C()
zy.eat()
#类方法
C.play()
#静态方法
C.say()
