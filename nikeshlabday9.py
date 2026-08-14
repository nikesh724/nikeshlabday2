#inheritance
#single inheritance
'''class CSK:
    def fun1(self):
        print("CSK team")
class Dhoni (CSK):
    def fun2(self):
        print("GOAT")
c = CSK()
d = Dhoni()
c.fun1()
d.fun1()
d.fun2()'''

#Hiear inheritance
'''class theatre:
    def fun1(self):
        print("movie")
class dare_devil(theatre):
    def fun2(self):
        print("dare devil")
class spider_man(theatre):
    def fun3(self):
        print("spider man")
t = theatre()
d = dare_devil()
s = spider_man()
t.fun1()
d.fun1()
d.fun2()
s.fun1()
s.fun3()'''

#multilevel inheritance
'''class grandfather:
    def fun1(self):
        print("family")
class father (grandfather):
    def fun2(self):
        print("father")
class son (father):
    def fun3(self):
        print("son")

g = grandfather()
f = father()
s = son()
g.fun1()
f.fun1()
f.fun2()
s.fun1()
s.fun2()
s.fun3()'''

#hybrid inheritance
'''class livewire:
    def fun1(self):
        print("livewire")
class mother(livewire):
    def fun2(self):
        print("mother")
class father(livewire):
    def fun3(self):
        print("father")
class you (father,mother):
    def fun4(self):
        print("you")
l = livewire()
m = mother()
f = father()
y = you()
l.fun1()
m.fun1()
m.fun2()
f.fun1()
f.fun3()
y.fun1()
y.fun2()
y.fun3()
y.fun4()'''

#multiple inheritance
'''class mother:
    def fun1(self):
        print("mother")
class father(mother):
    def fun2(self):
        print("father")
class you (father,mother):
    def fun3(self):
        print("you")

m = mother()
f = father()
y = you()
m.fun1()
f.fun1()
f.fun2()
y.fun1()
y.fun2()
y.fun3()'''

#polymorphism
#overloading
'''class ram:
    def add (self,a,b=0,c=0):
        return a+b+c
r = ram()
print(r.add(1))
print(r.add(2,3,4))
print(r.add(5,6,7))'''

#args
'''class ram:
    def add (self,*args):
        print(sum(args))
r = ram()
r.add(1,2,4)
r.add(3,5,6)'''

#abstraction
'''from abc import ABC,abstractmethod
class nikesh(ABC):
    @abstractmethod
    def fun1(self):
        pass
class activity(nikesh):
    def fun1(self):
        print("talking")

a = activity()
a.fun1()'''

#encapsulation
#public
'''class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student = student("nikesh",22)
print(student.name)'''

#private
class Bank_account():
    def __init__(self,balance):
        self.balance = balance
#creater method
def _get_ balance(self):
    return self.balance
#setter method
def _set_balance(self,amount):
    if amount >= 0:
        self.balance = amount

    else:
        print("invalid amount")
acc = Bank_account(1000)
print("initial balance:",acc.get_ balance())
acc.get balance(2000)
print("updated balance:",acc.get balance())
acc.set_balance(-500)


