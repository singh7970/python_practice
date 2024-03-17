# from collections import Counter
# s="hello worksdjbvajdballd"
# l=Counter(s)
# o=[]
# for x ,j in l.items():
#     o.append(j)
#     print(f'{x} {j}')


input = input("Enter a string: ")
dict = {}
for char in input:
    if char in dict:
        dict[char] += 1
    else:
       dict[char] = 1

print(dict)
# for char, frequency in reversed(sorted(dict.items())):
#     print(char,frequency)
# for i in sorted(dict.items()):
#     print(i)

    
    
    

        




 

 