#program for demonstating calss leel methods 
class Employee:
    @classmethod
    def getcompanydata(cls):#class level method
        Employee.companyname=input("Enter company name:")
        Employee.companyaddress=input("Enter company address:")

        def dispcompanydata(self):#class level method
            print("Company name:",Employee.companyname)
            print("Company address:",Employee.companyaddress)
            def getemployeedata(self):#instance method
                self.eno=int(input("Enter employee number:"))
                self.ename=input("Enter employee name:")
                self.salary=int(input("Enter employee salary:"))

                #main program
e1=Employee()#object creation
e2=Employee()#object creation
e1.getcompanydata()#calling class level method using object e1
e2.getcompanydata()#calling class level method using object e2