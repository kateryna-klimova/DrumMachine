#!/usr/bin/env python

"""Main Script: Google Home and ISRs"""

# Imports
from Adafruit_IO import MQTTClient
from time import sleep
import os
import os.path
import RPi.GPIO as GPIO
import os
import os.path

# Global variables
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
drum_pad_mode = 'blank'
ADAFRUIT_IO_USERNAME = "katerynaklimova"
ADAFRUIT_IO_KEY = "e2eee5f63ba54e26b3fb8bb70dd4bd09"

# Here comes your function definitions

# Subscribes to the Adafruit stream
def connected(client):
    client.subscribe('google_commands')

# this gets called every time a message is received
def message(client, feed_id, payload): #proces the commands from Google $
     global drum_pad_mode
     if payload == "mode piano":
        sleep(1)
        #os.system('aplay -D bluealsa ~/Desktop/project/piano2.wav')
        drum_pad_mode = 'piano'
        print ("Mode set to " + drum_pad_mode)
     elif payload == "mode drums":
        drum_pad_mode = 'drums'
        print ("Mode set to " + drum_pad_mode)
     else:
        print "Message from Google Home: %s" % payload

def callback1(channel):
    if drum_pad_mode == 'blank':
        #os.system('sonic_pi play 60')
        print "Playing from port 24 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'piano':
        #os.system('sonic_pi play 80')
        #os.system('aplay -D bluealsa ~/Desktop/project/piano2.wav')
        print "Playing from port 24 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'drums':
        #os.system('sonic_pi play 50')
        print "Playing from port 24 in mode %s" % drum_pad_mode

# Function defenitions end

def main():
        client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
        client.on_connect    = connected
        client.on_message    = message
        client.connect()
        GPIO.add_event_detect(24, GPIO.FALLING, callback=callback1, boun$
        GPIO.add_event_detect(23, GPIO.FALLING, callback=callback2, boun$
        client.loop_blocking()
        GPIO.cleanup()

if __name__ == "__main__":
        main()

