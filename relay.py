#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
#relay = 7
relay = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)
#relay = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
#GPIO.setup(rel,GPIO.OUT)

# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def callback(channel):
    if GPIO.input(channel):
        print ("Water Not Detected!")
        time.sleep(1)
               
    else:
        print ("Water Detected!")
    while True:
      for x in range(5):
    
            GPIO.output(relay, True)
            time.sleep(0.1)
            GPIO.output(relay, False)
            
      GPIO.output(relay,True)

      for x in range(4):
            GPIO.output(relay, True)
            time.sleep(0.05)
            GPIO.output(relay, False)
            time.sleep(0.05)
      GPIO.output(relay,True)
        
                
        
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
#




