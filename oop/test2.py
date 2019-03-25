class Student():
    name = "zy"
    age = 10

Student.__dict__

#实例化
zy = Student()
zy.__dict__
print(zy.name)