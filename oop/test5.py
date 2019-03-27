#多继承
#子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("swimming.......")
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("flying........")

class Person():
    def __init__(self,name):
        self.name = name
        print("Person")
    def run(self):
        print("running.......")

    def work(self):
        print("working.......")
 #多继承
class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name
 #单继承
class Student(Person):

    def __init__(self,name):
        #构造函数的两种调用方法
        Person.__init__(self, name)
        super(Student,self).__init__(name)
        #初始化数据
        self.name = 'zy'
        self.age = 18
        self.add = "china"
        print("Student")

s = SuperMan('zy')
s.fly()
s.swim()
s.run()
print("*"*80)
stu = Student('C')
#构造函数调动顺序
#子类没有构造方法，则自动向上查找

#多态代码Mixin的使用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SuperMan1Mixin():
    def work(self):
        print("working.......")

s1 = SuperMan1Mixin()
s1.work()

#help 案例
#我想知道setattr的具体使用
help(setattr)
