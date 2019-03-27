#继承的语法
#在python中任何类都有一个共同的父类 object
class Person():
    name = 'zy'
    _petname = 'yy'#是保护的，子类可用，但不能公用
    age = 18
    gender = "男"
    _score = 0
    __hobby = 'eat'#私有成员
    sex = 9
    def sleep(self):
        print("sleeping.......")
    def work(self):
        print("working.......")
#父类写在括号内
class Teacher(Person):
    Teacher_id ='007'
    sex = 8
    def make_test(self):
        print("开始考试了哦···")
        print(t._petname)
    def work(self):
        #扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)
        #super代表得到父类
        super().work()
        self.make_test()

t = Teacher()
t.work() #重写父类调用
print(t.name)
print(Teacher.name)
Teacher.make_test(t.name)
print(t.Teacher_id)
print(t.sex) #子类和父类有相同成员，则优先使用子类成员
t.sleep()




