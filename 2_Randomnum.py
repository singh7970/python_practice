# import random
# x = random.randint(1,10)
# print("Randint",x)
# print(random.randrange(1,4))
# l=[12,123,112,3443,2343,4,46,6,54,]
# print(random.choice(l))

# print(random.random())
# p=[12,123,112,3443,2343,4,46,6,54]
# random.shuffle(p)
# print(p)
# print("1020012")
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
