n=int(input("Enter the number"))#user input number 
print(" 1 bin")
print(" 2 oct")
print(" 3 hex")
o=int(input("Enter the operation"))#user input number 
if o==1:
    print(bin(n)[2:],"binary")#Convert to binary form
elif o==2:    
    print(oct(n)[2:],"octal")#Convert to ocatl form
elif o==3:
    print(hex(n)[2:],"hexadecimal")#Convert to hexadecimal  form
else:
    print("select right choice :")    