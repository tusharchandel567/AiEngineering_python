#writw a pyhton program this is plaindrome or not 
def is_palindrome(s):
    return s == s[::-1]

#main program
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")