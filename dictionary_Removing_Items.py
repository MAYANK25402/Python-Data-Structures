#  using the pop method

dict={"hello":"world","all":"good","get in":"here"}
print("elements without any deletion")
print(dict)
dict.pop("get in")
print("elements after the elimination")
print(dict)
print("-------------------------------------")

#  pop the item

dict={"hello":"world","all":"good","get in":"here"}
print("values without popping")
print(dict)
dict.popitem()    # poitem function donot take any argument with it it simply pops the value on its own
print("values after popping")
print(dict)
print("-------------------------------------")

# using the del function or the keyword

dict={"hello":"world","all":"good","get in":"here"}
print("elements before deletion")
print(dict)
del dict["get in"]
print("elements after the deletion")
print(dict)
print("-------------------------------------")

#  del function or keyword to delete the complete dictionary

dict={"hello":"world","all":"good","get in":"here"}
del dict
print(dict) # no elements will be present in it after del keyword is used
print("-------------------------------------")

# using the clear function

dict={"hello":"world","all":"good","get in":"here"}
dict.clear()
print(dict)