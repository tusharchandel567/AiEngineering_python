#write a pthon program a given num is Armstrong or not 
num = int (input("Enter this number , what scroll your mind currently try to enter"))
temp = num
digits = len(str(num))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //=10

    if sum == num:
        print("Armstrong Number")
    else:
        print("Not a Armstrong number ")
