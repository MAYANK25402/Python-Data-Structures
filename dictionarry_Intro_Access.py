# simple accessing the items of the dictionary

dict = {"hello": "again", "I": "am", "good": "too"}
print(type(dict))
print(dict)
print("-------------------------------------------------------")

# Accessing a single item in the dictionary

dict = {"hello": "again", "I": "am", "good": "too"}
print(dict["hello"])
print(dict["good"])  # it will print the values of the item that is after the input that we will give
print("-------------------------------------------------------")

# duplicates not allowed

dict = {"my": "name", "is": "arun", "is": "mayank"}
dict2 = {"duplicate": "is", "not": "considered", "not": "allowed"}
print(dict)
print(dict2)  # in this the duplicate value is not allowed

# its meaning is that if two keys in dictionary starts with the same word, and ends with different words

# then the last word will be considered only as prvious words will not be considered
