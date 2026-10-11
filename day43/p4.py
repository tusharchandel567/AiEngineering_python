#function for calculating factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    #main program
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print("Factorial of", num, "is:", fact)