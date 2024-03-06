# a=[2,1,2,3,8,5,2,2,2,2,6]
# for i in a:
#     a.remove(i)
# print(a)
# print(a.count(2))


# x=['1','2','3']
# y=x[1]+x[2]
# print(y)

# b=123
# c=563454
# print(b>c)

                                 #QUESTION 
                  # print the number whos count is  one
l=[1,2,2,3,3,3,4,4,1,5,6]
nl=[]
for num in l:
    if l.count(num)==1:
        nl.append(num)
print(nl)        