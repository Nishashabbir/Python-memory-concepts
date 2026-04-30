
import datetime 
print(datetime.datetime.now())

# you can also use this in a way like : 

waqt=datetime.datetime.now()
print(waqt.year)
print(waqt.timestamp())
print(waqt.strftime("%A"))  #this gives you the day 

# datetime object

# to create the datetime we can use the class datetime and pass three required arguments 

x=datetime.datetime(2020 , 1, 13)
print(x) #now it will convert it like this 2020-01-13 00:00:00

