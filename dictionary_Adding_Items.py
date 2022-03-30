# using the simple method to add items in the dictionary

dict={"hello":"world","how":"are"}
print("elements before adding the items")
print(dict)
dict["you"]="all"
print("elements after addition of new elements")
print(dict)
print("-------------------------------------")

# using the update method for addition

dict={"hello":"world","how":"are"}
print("elements before any addition")
print(dict)
dict.update({"you":"all"})
print("elements after the addition")
print(dict)
