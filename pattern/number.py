# Write a program to print the following pattern.
def num(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
num(n)