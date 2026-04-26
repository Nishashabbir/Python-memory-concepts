# import maths_utils as m 

# print(m.add(2,3))
# print(m.mult(4,5))
# print(m.subtract(10 ,5))

# using built in module to generate a random number 

# import random
# from math import sqrt 


# number=random.randint(1,100)
# print(number)

# # print(sqrt(49))
# result=sqrt(49) + sqrt(64)
# print(result)
def greet():
    print("Hello!")

if __name__ == "__main__":
    print("Running directly")
    greet()

import mod1 as u  #not utils.py 

# print(u.person1["age"])
import platform

x = platform.system()
# print(x) #windows


print(dir(platform))
