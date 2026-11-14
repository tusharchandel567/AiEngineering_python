#program for demonstarting instance methods in python classes
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
