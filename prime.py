num=int(input("Enter the  number"))
if num==1:

    print("it is note a prime number")
if num >1 :
    for i in range (2,num):
        if num % i ==0:
           
            print("it is note a prime number")  
 
            break
    else:
        print("it is prime ")    