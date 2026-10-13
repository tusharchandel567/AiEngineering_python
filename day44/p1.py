#program for demonstrating the concept of possitional arguments and keyword arguments
def disstudeio(sno,sname,smarks):
    print("Student number:",sno)
    print("Student name:",sname)
    print("Student marks:",smarks)

    #main
    print("Calling function with positional arguments:")
    disstudeio(1,"John",85)
    print("Calling function with keyword arguments:")
    disstudeio(sname="Alice",smarks=90,sno=2)
    