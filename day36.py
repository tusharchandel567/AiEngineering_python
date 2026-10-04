aith1 = int(input("enter a number 1"))
full = input("enter a number 2 & number2 ")
aith2 = int(input("enter the number "))

match full:
    case"+":
        print("addition=",aith1+aith2)
    case"-":
                print("addition=",aith1-aith2)
    case"*":
                print("addition=",aith1*aith2)
    case"/":
                print("addition=",aith1/aith2)
    case _:
                print("enter invalids")