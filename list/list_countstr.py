'''Write a Python program to count the number of strings where the string length is 
2 or more and the first and last character are same from a given list of strings. 

 Sample List : ['abc', 'xyz', 'aba', '1221']
 Expected Result : 2'''


l= ['abc', 'zx','abaa', '1221','1211','3213']

count=0
for i in l:
        if  len(i)>=4 and i[0] == i[-1]:
        # if  i[0] =='a':
            
            count += 1
print(count)            
# c=l[2]
# print(c)
# print(c[1])
