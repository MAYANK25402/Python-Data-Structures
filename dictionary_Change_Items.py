# first using the basic key and value updation

dict={"mercedes":"benz","model":"AMG gt s+","year":2000}
print("dictionay without doing updation process")
print(dict)
x=dict["year"]=2010
print("dictionary after updating the value")
print(x)
print(dict)
print("------------------------------------------------")

# using the update() function to change

dict={"hello":"everyone","all":"good","work":"hard"}
print("dictonary without any updation process")
print(dict)
dict.update({"work":"fine"})
print("dictionary after the updation is done")
print(dict)

    # in this we simply have to use the update function to update the item value