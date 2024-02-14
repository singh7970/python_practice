n=int(input("Enter the number"))#user input number 
print(" 1 bin")
print(" 2 oct")
print(" 3 hex")

print(bin(n)[2:],"binary")#Convert to binary form
print(oct(n)[2:],"octal")#Convert to ocatl form
print(hex(n)[2:],"hexadecimal")#Convert to hexadecimal  form