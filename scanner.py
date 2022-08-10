#Modules
import socket
import subprocess
import datetime
import os

#Clearscreen
subprocess.call('clear'  )

#Get input
server  = input("Enter port a Host :"  )
remoteserverip =  socket.gethostbyname(server)

#Banner
print (" " * 70)
print ("please wait Procesing..." ,remoteserverip)
print (" " * 70)
 #Date and Time
dt = datetime.now()

#Specify Ports

try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET,socket.sock.STREAM)
        res = sock.connect_ex((remoteserverip.port))
        if res == 0:
            print("port{} : open".format(port)) 
            sock.close()
except:
                print("Error")
#Check Time
dt1 = datetime.now()

#Time Elapsed
t = dt1-dt
print("Completed In: " ,t)






