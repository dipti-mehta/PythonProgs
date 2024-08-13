# dict constructor
d1 = dict(name="John", age=36, country="Norway")
print(d1)

# Access dictionary items
d2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = d2["model"]
'''There is also a method called get() 
that will give you the same result:
 x = d2.get("model")
 
 The keys() method will return a list of all the keys in the dictionary.
 x = d2.keys() 
 The values() method will return a list of all the values in the dictionary.
Example
Get a list of the values:
x = d2.values() '''
print(x)

# Adding new items------------------------------
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# items method----------------------------------------
# The items() method will return each item in a dictionary, as tuples in a list.
# Example
#
# Get a list of the key:value pairs
# x = thisdict.items()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

# presence of item-----------------------------
'''Check if Key Exists : To determine if a specified 
key is present in a dictionary use the in keyword:
Check if "model" is present in the dictionary:'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

The popitem() method removes the last inserted item (in versions before 3.7, a random 
item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) """
