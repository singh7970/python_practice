'''Write a Python program to print a specified list after 
removing the 0th, 4th and 5th elements. 

Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''

l1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l1.pop(5)
l1.pop(4)
l1.pop(0)

print(l1)