l = []
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# for i in 
# l.append(a)
# l.append(b)
# l.append(c)
# l.append(d)
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    l.append(num)
 

print(l)
s = sorted(l)
r = list(reversed(s))
print(r)
