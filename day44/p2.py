def dispstdinfo(sno,sname,marks,crs="Python"):
    print("Student number:",sno)
    print("Student name:",sname)
    print("Student marks:",marks)
    print("Student course:",crs)

    #main Program
    print("+"*50)
    print("\tsno\t\tsname\t\tmarks\t\tcrs")
    dispstdinfo(1,"John",85)
    dispstdinfo(2,"Alice",90,"Java")
    dispstdinfo(3,"Bob",75)
    print("+"*50)
    print("\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format(1,"John",85,"Python"))
    print(dispstdinfo)