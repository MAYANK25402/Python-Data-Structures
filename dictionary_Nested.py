# first method to access the nested dictionary keys ans values

dict={"child1":{"name":"mayank","age":20},"child2":{"name":"ram","age":21},"child3":{"name":"shayam","age":22}}
print("the value of the diffrent dictionaries are in a same dictionary")
print(dict)
print("--------------------------------")
# in this method there are many dictonaries get combined in a single dictionary


# another methos of using nested dictionary is by creating seperate dictionary

dict1={"hello":"again","from":"india"}
dict2={"namaste":"again","from":"america"}
dict3={"hi":"everyone","from":"australia"}

my_dict={"dict1":dict1,"dict2":dict2,"dict3":dict3}
print(my_dict)   # in this seperate dictionaries are created

#  in final dictionary we called all the dictionaries in a single dictionay function my_dict() created by us