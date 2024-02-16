print("Calculator")
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
print("select your choice")
print("1___+")
print("2___-")
print("3___*")
print("4___/")
choice =input("Enter the operation : ")
if choice=="1":
    print(num1+num2)
elif choice=="2":
    print(num1-num2)
elif choice=='3':
    print(num1*num2)
elif choice == '4':
    print(num1/num2)
else:
    print("Enter Right choice")








