# access of a single key

dict = {"mercedes": 2000, "audi": 2001, "bmw": 2002}
print(dict)
x = dict["mercedes"]
print(x)
print("1-------------------------------------------------------")

# access using get method

dict2 = {"hello": "world", "i": "am", 20: "years", "in": "age"}
print(dict2)
x = dict2.get("i")
print(x)
print("2-------------------------------------------------------")

# print all the keys in dictionay

dict2 = {"hello": "world", "i": "am", 20: "years", "in": "age"}
print(dict2)
x = dict2.keys()
print(x)  # in this we will simply get ll the key values of the whole dictionary
print("3-------------------------------------------------------")

# adding the new key in our dictionary / same can be done for the values also

dict3 = {"mercedes": "benz", "model": 2002, "colour": "black"}
x = dict3.keys()
print("dictionary without updation of another key")
print(x)
print(dict3)
dict3["shape"] = "original"
print("dictionary after updation")
print(x)
print(dict3)  # in this we update the keys and print the whole dictionary
print("4-------------------------------------------------------")

# printing values of the keys

dict3 = {"hello": "world", "it\'s": "alright"}
print(dict3)
print("now printing the values only")
x = dict3.values()
print(x)
print("5-------------------------------------------------------")


#  another method to print the whole dictionary [item method]

dict3 = {"hello": "world", "it\'s": "alright"}
print(dict3)
print("now printing using the item function")
x=dict3.items()
print(x)
print("6-------------------------------------------------------")


#  to check if the key is present in the dictionary or not

dict3 = {"hello": "world", "it\'s": "alright"}
if "hello" in dict3:
    print("yes!, hello named key is present in this dictionary")
else:
    print("no the key is not present in this dictionary")
