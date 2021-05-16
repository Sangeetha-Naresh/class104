from collections import Counter

data= "whitehatjr"

newdata = Counter(data)
print(type(newdata))
print(newdata)

new_list=newdata.items() #dictionary
print(type(new_list))
print(new_list)

values=newdata.values() #dictionary values
print(type(values))
print(values)