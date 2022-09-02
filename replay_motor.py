#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
#relay = 7
channel1 = 7
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel1, GPIO.OUT)
#relay = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
#GPIO.setup(rel,GPIO.OUT)

# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def callback(channel):
    if GPIO.input(channel):
        print ("Water Not Detected!")
        
               
    else:
        print ("Water Detected!")
        time.sleep(1)
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    try:
        motor_on(channel1)
        time.sleep(1)
        motor_off(channel1)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
    
                
        
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
#




