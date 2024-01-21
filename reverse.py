a=int(input("enter the NUMber"))

c=0
for i in range (1,len(str(a))+1):
    b=a%10
    c=c*10+b
    a=a//10
print(c)