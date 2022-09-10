class Student:
    company="hongze"
    count=0
    def __init__(self,name,score):
        self.name  = name
        self.score = score
        Student.count = Student.count+1
    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))
s1=Student("xufe",22)
s1.say_score()
print(dir(s1))
print(s1.__dict__)
print(isinstance(s1,object))
print(Student.company)
print(Student.count)
print('count is {0}:',Student.count)
