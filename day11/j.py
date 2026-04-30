
# python has the json module to work with the json format data 
# Example
# Convert from JSON to Python:

# this is a json data that we have to convert into the python 
import json

x =  '{ "name":"John", "age":30, "city":"New York"}' #this is in string and we want it to be in python dict 


# y=json.loads(x)
# print(y) #it will print a python dict 
# print(y.get("age"))
# print(y["age"])


# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

p={'name': 'John', 'age': 30, 'city': 'New York'}

x=json.dumps(p)
# print(x)


# converting the other python objects in the json form 

# x=print(json.dumps([1,3,4,5,6])) #list
# x=print(json.dumps((1,3,4,5,6))) #tuple
# x=print(json.dumps({"name": "John", "age": 30}))
# x=print(json.dumps(True))
# x=print(json.dumps(False))
# x=print(json.dumps(10))
# x=print(json.dumps(0.4))
# x=print(json.dumps(None))

# Convert a Python object containing all the legal data types:


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x)) #this will be without indentation ,  hard to read 

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:

# Example
# Use the indent parameter to define the numbers of indents:

print(json.dumps(x, indent=4)) #this will be with indentation quite easier to understand

# Use the separators parameter to change the default separator:
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(json.dumps(x, indent=4, sort_keys=True))