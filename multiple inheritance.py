class Father: 
    def f(self): 
        print("Father class") 
class Mother: 
    def m(self): 
        print("Mother class") 
class Child(Father, Mother): 
    def c(self): 
        print("Child class") 
obj = Child() 
obj.f() 
obj.m() 
obj.c() 
