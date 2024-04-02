# User will input (3ages).Find the oldest one
print("Enter the 3 number to find oldest")
a=int(input("Enter the number :"))
b=int(input("Enter the number:"))
c=int(input("Enter the number :"))
if (a<b and a<c):
    print("a is older")
elif (b<c and b<a):
    print("b is older")    
elif(c<a and c<b):
    print("c i older")
else:
    print("pass")    
