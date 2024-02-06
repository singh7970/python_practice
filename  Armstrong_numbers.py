print("------THIS NUMBER Is FOR ONLY 3 DIGITS-------")
a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
n = str(a) + str(b) + str(c)
l = len(n)


t=a**l,b**l,c**l
# p = int(''.join(map(str, t)))
# print(p)
# print(n)
s=str(sum(t))
print(type(s))
print(type(n))

# print(a**l,l,a)
# print(b**l,l,b)
# print(c**l,l,c)


if s==n:
    print("yes ::IT is  Armstrong numbers")
else:
    print("NO it is not Armstrong numbers")    

