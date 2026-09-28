#identity operator 
# two types 1. is 2. is not

a=10
b=20
print('valuse {} a {} b'.format(a,b))
c = a is b
print(c)
d = a is not b
print(d)

me,de=200,200
f= me is de 
print(f)
g = me is not de
print(g)

#ternary operator (if else )

#write a program findbiggest of twoi number check 

a=int(input("enter your first choose number"))
b=int(input("enter your second number you can choose "))
bv = a if a>b else b if b >a else "values are equal"
print("big({} ,{})".format(a,b,bv))