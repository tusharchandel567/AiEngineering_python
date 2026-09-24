#Bit wise complement operators
a=10
b=20
c=~a
print(c) #-11

#XOR operator
a=10
b=20
c=a^b
print(c) #30

#write a python program swap xor 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, "b =", b)

#write a python program swaping addition and subtraction
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)