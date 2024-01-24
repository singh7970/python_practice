# a=[161 ,182, 161, 154 ,176, 170, 167, 171, 170, 174]
# x=set(a)
# b=len(x)
# print(b)
# w=sum(x)
# print(w)
# avg=w/b
# print(avg) 


# n=int(input("Enter the number"))
# l=[]
# for i in range (1,n+1,1):
#     num=input(f"Enter the country name{i} :")
#     l.append(num)
# print(l)
# a=set(l)
# print(a)
# print(len(a))

n = int(input("Enter the nuber"))
Country = set()
for i in range(n):
    Country.add(input("Enter the countery"))
print(len(Country))
 