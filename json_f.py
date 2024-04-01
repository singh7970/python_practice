# ''''''Write a Python program to convert JSON data to Python object.
'''
import json

data = '{"name":"priyanshu","class":"1","Age":"6"}'
parsed_data = json.loads(data)
print(parsed_data)
'''

# Convert from Python to JSON:
import json
# x={1:"a",2:"b",3:"c"}
# y=json.dumps(x)
# print(y)
# print(type(y))
