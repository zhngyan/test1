"""
定义一个学生类，用来形容学生
"""
#定义一个空的类
class Student():
    pass
#定义一个对象
zy = Student()

class PythonStundet():
    name  = None
    age = None
    sex = None
    course = "Python"

    def doHonmework(self):
        print("做作业")
        return None  #推荐在函数末位使用return
#实例化
zy = PythonStundet()
print(zy.age)
print(zy.name)
#成员函数的调用没有传递参数
zy.doHonmework()