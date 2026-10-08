#write a python program which display 1 to n multiple table 
n = int (input("enter you num to start multipliaction "))
if(n<=0):
    print("{} is Invalid input ",format(n))
else :
    #outer loop - supply numbers
    for num in range(1,n+1):
        print("--------------------------")
        print("multiable table for {}",format(num))
        print("---------------------------")
        for i in range(1,11):
        
            print("\t {} x {} = {} ".format(num,i,num*i))
            
            