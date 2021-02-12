#import Section
import time
import datetime
import socket
import geocoder

#Variable Preset Declaration
ts = time.time()
str_ts = str(ts)
ts = str_ts.replace('.','')
# ip = socket.gethostbyname(socket.gethostname())
# g = geocoder.ip('me')
# enc = input("Enter the Data to Encrypt!")

# print("User IP",ip)
# print("User Timestamp",ts)
# print(g.latlng)
# print('Your Text',enc)
# print (ts)



ch = 'Hi Granny'
listA = []
final = ''
keyA = int(ts) % 126
if(keyA == 0):
    keyA = (int(ts)*3) % 126

for i in ch:
    val  = ord(i) +  keyA     #16131070059674842
    print('ts',int(ts))
    print(i,':', val , ':', chr(val))
    final += str(chr(val))
print(final)


  
# Using chr()+ord() 
# prints P 
# x = chr(ord(ch) -51) 
  
# print ("The incremented character value is : ",end="") 
# print (x) 

