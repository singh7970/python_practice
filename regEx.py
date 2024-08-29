import re 
txt="The rain in spain"
# x=re.search("^The.*spain$",txt)
# x=re.findall("he",txt)
x=re.findall("[a-h]",txt)
print(x)