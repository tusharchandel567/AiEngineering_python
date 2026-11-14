#types of methods in a class of python 
#1. instance method , 2. class levemethods , 3. ststic methods 
#instance method: instance methods are the most common type of methods in python classes. They take self as the first parameter, which refers to the instance of the class. Instance methods can access and modify the attributes of the instance.
#class method: class methods are methods that are bound to the class and not the instance of the class. They take cls as the first parameter, which refers to the class itself. Class methods can access and modify the class attributes.
#static method: static methods are methods that are not bound to the class or the instance of the class. They do not take any special first parameter. Static methods can access neither the class nor the instance attributes.

#program demonstrating instance methods 
#instanceMethodx1.py

class Student:
    def getstuddata(self):#instance method
        print("id of current in getsstuddata()=",id(self))
        self.sno=int(input("Enter student number:"))
        self.sname=input("Enter student name:")
        self.marks=int(input("Enter student marks:"))
    def dispstuddata(self):#instance method
        print("id of current in dispsstuddata()=",id(self))
        print("Student number:",self.sno)
        print("Student name:",self.sname)
        print("Student marks:",self.marks)
#main program
s1=Student()#object creation
s2=Student()#object creation
print("id of s1=",id(s1))
print("id of s2=",id(s2))
s1.getstuddata()#calling instance method using object s1
s2.getstuddata()#calling instance method using object s2
s1.dispstuddata()#calling instance method using object s1
s2.dispstuddata()#calling instance method using object s2
