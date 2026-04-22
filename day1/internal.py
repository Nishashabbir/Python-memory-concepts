
# these are just naming conventions for private variables in python but they are not really private and can be accessed outside the class using name mangling but it is not recommended to do so as it can lead to unexpected behavior and can break the encapsulation of the class

# Encapsulation (Not Strict in Python)

# Convention:

    # self._private
    # self.__very_private

# Single underscore → internal use
# Double underscore → name mangling

class A:
    def __init__(self):
        self.__x = 10

# Internally becomes:

# _A__x



class A:
    def __init__(self):
        self.__x = 10
# print(A().__dict__)


_x=20  #now here it is just a normal variable but when we use it inside a class it becomes a class variable and its behavior changes 
print(_x.__dict__)

