l=[]
n =int(input("Enter the nuber :"))

for i in range(10):
    n = n // 2
    p=n%2
    l.append(p)

print("old",l)
l.reverse()
print("new",l)