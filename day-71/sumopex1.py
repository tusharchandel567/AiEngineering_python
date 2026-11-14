#Program for adding of two numbers by using calsses and object with instance method 

class sum:
    def readvalues(self):#instance method
        self.a=int(input("Enter first number:"))
        self.b=int(input("Enter second number:"))
    def addvalues(self):#instance method
        self.sum=self.a+self.b
        def dispvalues(self):#instance method
            print("Sum of two numbers:",self.sum)

            #main program
s1=sum()#object creation
s1.readvalues()
s1.addvalues()
s1.dispvalues() 
