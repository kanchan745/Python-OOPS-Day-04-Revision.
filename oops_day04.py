#del keyword 

#used to delete objects properties or objects itself

'''class   Student:
    def __init__(self,name):
        self.name = name 
s1 = Student("Kanchan")
#del s1.name
print(s1.name)'''

#private (like) attributes and methods


'''class Account:
    def __init__(self ,acc_password, acc_no):
        self.acc_no = acc_no
        self.__acc_password = acc_password #use __ to make a private attribute
        #we can access it outside the class
        
    def reset_pass(self):
        print(self.__acc_password)
             
        
acc1 = Account ("55555555",12563)
acc1.reset_pass()'''
#print(acc1.acc_no, acc1.acc_password)

        
# class Person:
#     __name = "Anonymous" # attribute private

# p1 = Person()
# print(p1.__name)           
    
'''Method private'''
'''class Person:
    __name = "Anonymous"
    
    def __hello(self):
        print("Hello Person") 
        
    def welcome(self):
        self.__hello() 
            
p1 = Person()
print(p1.welcome() )'''   

#conceptual implementation in python:

#inheritance : When one class (child/ derived)  derives the properties and methods of another class(parebt/base)

'''class Car:
    colour = 'Blue'
    @staticmethod
    def start():
        print("Car started.....")
    
    @staticmethod
    def stop():
        print('car stopped......')
        
class ToyotaCarr(Car):
    def __init__(self, name):
        self.name = name 
        

car1 = ToyotaCarr("fortuner")
# print(car1.name) 
# car1.start()
# car1.stop()  
             
car2 = ToyotaCarr("prius")
print("\n",car2.name) 
print(car2.colour)'''

#Types of inheritance -> single , multi-level and multiple inheritance
'''single - base to derive class'''
'''Multi-level inheritance : base - derive (parent)-derive (child)'''

#multilevel inheritance 
'''class Car:
    @staticmethod 
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print('Car stoped..')
        
class ToyotaCar(Car):
    def __init__(self,brand) :
        self.brand = brand
        
class Fortuner (ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner ("petrol")
print(car1.type)
car1 = ToyotaCar("Fortuner") 
print(car1.brand)

car1.start()   '''  

#multiple inheritance : when a class is derived from more than one base class
'''class A:
    var_a = "Welcome to class A"      

class B :
    var_b = "Welcome to class B"
    
class C(A, B):
    var_c = "Welcome to class c"
    
check =  C()
print(check.var_c)            
print(check.var_a) 
print(check.var_b) '''

#Super method....: super() method is used to access methods of the parent class means  inside inheritance ->parent method
 

'''class Car :
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started .")
    
    @staticmethod 
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name ,type): 
     self.name = name 
     super().__init__(type)
     super().start()
     
car1 = ToyotaCar("Prius", "diesel")        
print(car1.type, car1.name)    '''

#Class method : a class method is bound to the class and receives the class as an implicit first argument .
#Static method can't access or modify class state and generally for utility ...

'''class Person :
    name = "Anonymous"
    
    def change_name (self, name ) :
        self.name = name 
p1 = Person()
p1.change_name("Kanchan Shakya")
print(p1.name)
print(Person.name)  '''

#Example of class method
#1st Way.......
class Person:
    name = "Anonymous"
    
    def change_name(self,name) :
        Person.name  = name 
        
p1 = Person()
p1.change_name("Kanchan")
print(Person.name)                            
           
        
        
            


            
'''Private attributes and methods are meant to be used only within the class and aren't accessible from outside the class'''
