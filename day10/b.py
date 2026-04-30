import a
import a #even if you import a module twice , it loads only once and then it sees from sys.modules avoiding reexecution
import importlib
import a

importlib.reload(a) #if you need to reload it , you can forcefullly do that 

# print("B:" ,__name__ )