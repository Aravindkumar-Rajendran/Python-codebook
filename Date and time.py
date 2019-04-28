#importing library
from datetime import datetime

#assigning object
dt = datetime.now()

#Calling the functions with object to get date and time
print ("Date and time: %s"%str(dt))

print ("Date: {0}/{1}/{2}".format(str(dt.day),str(dt.month),str(dt.year))) #Printing in Date format
print ("Time: {0}:{1}:{2}".format(str(dt.hour),str(dt.minute),str(dt.second))) #Printing in Time format



