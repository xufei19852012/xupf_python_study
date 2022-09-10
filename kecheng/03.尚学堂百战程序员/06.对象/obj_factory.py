#测试工厂模式

class CarFactory:
    def create_car(self,brand):
        if brand =="奔驰":
            return Benz()
        elif brand =="宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

class xufei():

    def __init__(self,name,age):
        self.name=name
        self.age = age
    pass

    def sayname(self):
        print("my name is{}:{} ".format(name,age))

    def __str__(self):
        return "这个类的名字是：{}".format(self.name)

    def say(self):
        print("xufei shuo is A")

    def __add__(self, other):
        if isinstance(other,xufei):
            return "{}--{}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"

p1 = xufei("gaoji",19)
p2 = xufei("anan",20)

x = p1+p2
print(x)
class bangyao(xufei):

    def __init__(self,wanju):
        self.wanju=wanju

    def say(self):
        super().say()
        print("banyao shuo is B")

xu =xufei("xufei",35)
yao = bangyao(3)
yao.say()


#print(xu)


#factory = CarFactory()
#c1 = factory.create_car("奔驰")
#c2 = factory.create_car("比亚迪")

#print(yao.__str__())
#print(c1)
#print(c2)
#dir(xu)
#print(xu.__dict__)
#print(xu.__class__)
#print(xu.__dir__)
#print(xu.__init_subclass__())
#print(yao.__hash__())
#print(xu.__mro__)
#print(yao.__class__.__mro__)
#print(yao.__dict__)
#print(object.__class__)
#print(object.__dict__)

