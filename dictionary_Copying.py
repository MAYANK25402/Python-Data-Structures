# first using the copy() method

dict = {"hello": "world", "once": "again"}
dict2 = dict.copy()
print(dict2)
print("--------------------------")

# using the dict function

thisdict = {"hey": "hello", "welcome": "you all"}
mydict = dict(thisdict)
print(thisdict)


# it will show us the error because dict() function is not defined in the dictionary