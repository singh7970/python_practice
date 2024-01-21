import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    
string, max_width = input("Enter the random string"), int(input("Enter the number you want width"))
result = wrap(string, max_width)
print(result)