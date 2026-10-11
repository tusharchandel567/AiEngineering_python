#write a python program to print function to calculate simple interset and total amount to pay 
def simpleint():
    p=int(input("Enter the principal amount: "))
    r=float(input("Enter the rate of interest: "))
    t=int(input("Enter the time in years: "))
    si=(p*r*t)/100
    total_amount=p+si
    print("Simple Interest is: ",si)
    print("Total Amount to pay is: ",total_amount)

#main program
simpleint()