'''1.Write a Python script to sort (ascending and descending) a dictionary by value. '''


my_dict = {"alok": 10, "ayush": 30, "abyerna": 20, "anjali": 70, "shoaib": 100}


print("\nSorted dictionary by values in ascending order:")
for key, value in sorted(my_dict.items(), key=lambda item: item[1]):
    print(key, ":", value)

print("\nSorted dictionary by values in descending order:")
for key, value in sorted(my_dict.items(), key=lambda item: item[1], reverse=True):
    print(key, ":", value)
