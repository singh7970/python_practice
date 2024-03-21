'''
Write a Python function that takes two lists and returns True 
if they have at least one common member.

'''
def common(list1,list2):
    l1=set(list1)
    l2=set(list2)
    l3=l1.intersection(l2)
    if len(l3)==0:
        print(True)
    else:
         print(False)   

list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10, ]
common(list1,list2)





    

