
# Loop Variable Behavior (Critical Concept)
# for i in range(5):
#     pass

# print(i) #it prints 4  as  Variable still exists. Loop does not create new scope.



# 15 — Mutation During Loop (Danger Zone)

# lst = [1,2,3]

# for x in lst: #it means for every iteration make those changes which result in inifinit as 100 keeps appending and elements are added 
#     lst.append(100)

# challenge : 
lst = [1,2,3]

for x in lst:
    x = x * 10  #here variables are reassigned and new objects created in the memory  , but python still points to the old objects 


# Assignment → changes variable not objects 
# Mutation → changes object