#Methods has been explained.....
print("--------Methods has been explained.....----------")
class Calcultaion:
    print("---------proper usage of method----------")
    result=0
    def sum(self,start,end):
        for i in range(start,end):
            self.result+=i
        return self.result

    print("--------retuns none in below scearios..--------")
    def learn(self):
        return

    def learn2(self):
        pass

    print("------return can return multiple values--------------")

    def learn3(self,a,b):
        return a if a>b else b

    def learn4(self):
        return 1,2,3,4

#Creating an object....
print("---------Object has been created to use the above methods---------")
c=Calcultaion()
print(c.sum(1,5))
print(c.learn())
print(c.learn2())
print(c.learn3(4,3))
print(c.learn4(),type(c.learn4()))


#Passing arguement to the method
print("--------Passing arguement to the method [method-1.positional argument]-------")
def sum(a,b=10):
    print("Positional arguments type 1 : " ,a,b)

sum(100)

sum(100,200)#the 10 exist will be overridden


print("--------Passing arguement to the method [method-2.keyword argument]-------")
def amma(s,v):
    print("Keyword arguments are : ",s,v)

amma(s=10,v=1000)

print("--------Passing arguement to the method [method-3.Positional + Keyword argument]-------")
def mix(a,b,c):
    print("Mixing positional : ",a,b,c)

mix(100,b=200,c=300)#works as there is no confusion.
#mix(100,b=200,300)#It is not possible we have to mention the positional first then kw arguments.

#Inheritance part-2
print("-----Inheritance part-2,Super keyword,Variable accessing------- ")
#To invoke the parent class variables,methods,parent class constructor......
a,b=10,20
class Myclass():
        a,b=100,200
        x,y=1,2
""" def myMeth(self):
        print("Parent class method is called.....")

    def __init__(self):
        print("Parent calss constructor called........")"""

class Subclass(Myclass):
    a,b=1000,2000
    def meth(self,a,b):
        a,b=10000,20000
        print("Global variables : ",globals()['a'],globals()['b'])
        print("Parent class variables with seld kw : ",self.x,self.y,"Parent class variables with super() : ",super().a,super().b)
        #self kw won't work in sub class to use the parent class variable when the sub and parent has the same named variables.
        print("sub class specific variables with same name :" ,self.a,self.b)
        print("Local varibales : ",a,b)
""" super().myMeth()
    super().__init__()
    Myclass.__init__()"""


s=Subclass()
s.meth(1,2)

#VVVVIMMMMPPPP
#calling parent class constructor from the child class.
#Note : parent class const should always be called inside the child class const or child class meth

#if child and parent doensn't have the constructor then that is not a problem
#case 1
print("----case..1------")
class x :
    a=10
    

class y(x):
        print(super().a)

yobj = y()


#case 2
print("----case..2------")
class x :
    a=10
    def __init__(self):
        print("Parent const--")

class y(x):
        print(super().a)

yobj = y() #zero parametrised parent const will be get called from child obj creation

#if child has const and parent has const then we can call any one i.e fine
#case 3
print("----case..3------")
class x :
    a=10
    def __init__(self):
        print("Parent const--")

class y(x):
    def __init__(self):
        print("Child constr")
        super().__init__()
        print(super().a)

yobj = y() #zero parametrised child const is called.

print("----case..4------")
#case 4
#if parent constructor with params and child has no const , then while creating child obj we have to pass the required args for parent constructor
class x :
    a=10
    def __init__(self,var):
        print("Parent const--")

class y(x):
    def m(self):
        super().__init__(10)

yobj = y(10)
yobj.m()

print("----case..5------")
#if child has parametrised const and parent also has const then we can call any one i.e fine
#case 5 :
#here as we can see I can't overload the constructor we can have only one constructor in python
#if we have overloaded also the latest written constructor will be picked.
#so that first two parent constructors are commented out.
#when the child class has the constructor then we should not actually call the parent class constructor for child obj creation 
#--i.e not even possible also but that's possible when the child has no constructor.
class x :
    a=10
    """def __init__(self,var):
        print("Parent const1--")
    def __init__(self,var,var1):
        print("Parent const2--")"""
    
    def __init__(self,var,var1,var2):
        print("Parent const3--")

class y(x):
    def __init__(self,var):
        print("Child const---")
    def m(self):
        super().__init__(10,10,10)

yobj = y(4)
yobj.m()





