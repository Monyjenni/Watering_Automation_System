#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
#channel1 = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
#GPIO.setup(channel1, GPIO.OUT)


# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def callback(channel):
    if GPIO.input(channel):
        print ("Water Not Detected!")
        #relay.toggle()
        #print("relay on")
    
                
    else:
        print ("Water Detected!")
# importing required libraries

import mysql.connector

dataBase = mysql.connector.connect(
  # the username of our sql

  host ="localhost",

  user ="root",
  #here the password is blank because it is developed for free.

  passwd =""
)
 

print(dataBase)

  
# Disconnecting from the server
dataBase.close()
#def motor_on(pin):
   # GPIO.output(pin, GPIO.HIGH)  # Turn motor on


#def motor_off(pin):
    #GPIO.output(pin, GPIO.LOW)  # Turn motor off


#if __name__ == '__main__':
   # try:
       # motor_on(channel1)
       # time.sleep(1)
       # motor_off(channel1)
      #  time.sleep(1)
       # GPIO.cleanup()
    #except KeyboardInterrupt:
       # GPIO.cleanup()
    

 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
    #give the script rest
        time.sleep(1)
