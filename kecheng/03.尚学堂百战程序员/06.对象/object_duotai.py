class man:
    def eat(self):
        print("e l chifan")
    pass
class Chinese(man):
    def eat(self):
        print("kuaizi")
    pass

class English(man):
    def eat(self):
        print("chazi")
    pass

class yindu(man):
    def eat(self):
        print("sou")
    pass

def maneat(m):
    if isinstance(m,man):
        m.eat()
    else:
        print("bu neng chifan")
        '''
    elif isinstance(m,Chinese):
        m.eat()
    elif isinstance(m,English):
        m.eat()
    elif isinstance(m,yindu):
        m.eat()
        '''


maneat(English())
maneat(yindu())