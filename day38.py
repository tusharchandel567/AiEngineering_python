#while loop 

#write a python program to cheeck whether char display while loop is present in the given string or not
s="python"
for char in s:
    if char == 'o':
        print("Character 'o' is present in the string.")
        break
else:
    print("Character 'o' is not present in the string.")

    #write a python program tonumerical integer value and generate a multiplication table by using for loop

    mul = int(input("Enter a number to generate its multiplication table: "))
    if(mul<=0):
      print("please enter a positive {}".format(mul))
    else:
        print("Multiplication table of", mul)
        for i in range(1, 11):
            print(mul, "x", i, "=", mul * i)    
            


    