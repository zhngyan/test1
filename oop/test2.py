#此案例说明：
#类实例的属性和其对象的实例的属性不对对象的实例属性赋值的前提下
#指向同一个变量
class Student():
    name = "zy"
    age = 10

    #注意say的写法，参数有一个self
    def say(self):
        self.name = "gzy"
        self.age = 18
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def say1(s):
        s.name = "zy"
        s.age = 20
        print("my name is {0}".format(s.name))
        print("my age is {0}".format(s.age))

#此时，Student成为类实例
print(Student.name)
print(Student.age)
#id 可以两个变量是否相同
print(id(Student.name))
print(id(Student.age))

print("*"* 20)
a = Student()
a.say()
a.say1()
print("*"* 20)

#查看所有的属性
print(Student.__dict__)
print(a.__dict__)
a.name = '11'
a.age = 20
print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*"* 80)

class Teacher():
    name = "zy"
    age = "25"

    def say2(self):
        self.name = 'LL'
        self.age = 90
        print("my name is {0}".format(self.name))
        #调用类的成员变量需要用__class__
        print("my age is {0}".format(self.age))
    def say3():
        print(__class__.name)
        print(__class__.age)
        print("hello,see you again")

t = Teacher()
t.say2()
#调用绑定类函数使用类名
Teacher.say3()

#关于self的案例
print("*"* 80)
class Z():
    name = "zz"
    age = 13

    def __init__(self):
        self.name = "yy"
        self.age = 14

    def say4(self):
        print(self.name)
        print(self.age)

class Y():
    name = "qq"
    age  = 15

z = Z()
# z.say4 系统会默认把a作为第一个参数传入函数
z.say4()
#此时，self被z代替掉
Z.say4(z)
#同时可以把z 作为参数传入
Z.say4(Z)
#此时，传入的是类实例Y，因为Y具有name 和age 属性，所以不会报错
Z.say4(Y)

#封装
print("*"* 80)
class Person():
    # 公有变量
    name = "zs"
    # 私有变量
    __age = "18"
    print(__age)

p = Person()
print(p.name)
print(Person.__dict__)
p._Person__age =19
print(p._Person__age)