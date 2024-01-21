import random 
print("Enter the number between 1-10")
comp=random.randint(1,10)
user=int(input("Enter the number"))
print("computer number",comp)
print("user number",user)

if (user > comp):
    print(f"{user} is greter then{ comp}")
elif (user <comp):
    print(f"{user} is less then {comp}")  
elif (user==comp):
    print("Your number is equal to computer number")      
else:
    print("retry")    
