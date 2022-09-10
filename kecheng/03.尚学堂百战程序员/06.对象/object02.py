class person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def say_age(self):
        print("我的年龄：{0}".format(self.age))

    def say_name(self):
        print("我的名字：{0}", self.name)
class Stuent(person):
    def __init__(self,name,age,score):
        person.__init__(self,name,age)
        self.score=score
    def say_name(self):
        print("报告，我的名字：{0}", self.name)
    pass

s=Stuent("xufei",12,34)
s.say_age()
s.say_name()
print(dir(s))
print(s.age)