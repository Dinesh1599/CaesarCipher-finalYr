#import Section
import time
import datetime
import socket
import geocoder

#Variable Preset Declaration
ts = time.time()
ip = socket.gethostbyname(socket.gethostname())
g = geocoder.ip('me')

print("User IP",ip)
print("User Timestamp",ts)
print(g.latlng)

