
from datetime import datetime
delta =  datetime.now() - datetime(1900 , 12 , 31) #delta is another object. which gives difference between two datetime objects
print("delta datatype looks like : ",delta)
print(delta.days," ",delta.seconds)
print("datetime.now = ",datetime.now())
whenever = datetime.strptime("2017-12-31","%Y-%m-%d") #input a datetime in a specified format. full details: strftime.org
print("Whenever = ", whenever)
print(whenever.strftime("%Y-%m-%d  %H:%M")) #prints in a format
