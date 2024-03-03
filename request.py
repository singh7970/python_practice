# import requests

# r = requests.get('https://www.youtube.com/watch?v=tb8gHvYlCFs&t=77s')
# print(r.json())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person("John Doe", 25)

print(f"{person1.name} is {person1.age} years old.")
person1.display_info()

