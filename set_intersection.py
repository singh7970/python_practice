# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# intersection_result = set1 & set2
# # Alternatively: intersection_result = set1.intersection(set2)

# print("Intersection Result:", intersection_result)
# s = set("Hacker")
# print (s.intersection("Rank"))
N1 = int(input("enter"))
storage1 = set(input("done").split())
N2 = int(input("2enter"))
storage2 = set(input("2done").split())
storage3 = storage1.intersection(storage2)
print(len(storage3))

