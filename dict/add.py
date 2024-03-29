dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
'''d=dic1|dic2
c=d|dic3
print(c)'''

dict3 = dic1.copy()
dict3.update(dic2)
print(dict3)



