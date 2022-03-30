# keys using the for loop

dict={"hello":"world","all":"good","get in":"here"}
for x in dict:
    print(x)
print("-------------------------------------")

# values using the for loop

dict={"hello":"world","all":"good","get in":"here"}
for x in dict:
    print(dict[x])
print("-------------------------------------")

# keys using the keys() function

dict={"hello":"world","all":"good","get in":"here"}
for x in dict.keys():
    print(x)
print("-------------------------------------")

# values using the values() function

dict={"hello":"world","all":"good","get in":"here"}
for x in dict.values():
    print(x)
print("-------------------------------------")

# both the values and the keys using the item() function

dict={"hello":"world","all":"good","get in":"here"}
for x,y in dict.items():
    print(x,y)

