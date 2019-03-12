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

# Setting global variables
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
drum_pad_mode = 'default'
ADAFRUIT_IO_USERNAME = "katerynaklimova"
ADAFRUIT_IO_KEY = "e2eee5f63ba54e26b3fb8bb70dd4bd09"

# Here comes your function definitions

# Subscribes to the Adafruit stream
def connected(client):
    client.subscribe('google_commands')

# this gets called every time a message is received
def message(client, feed_id, payload): #proces the commands from Google Home
     global drum_pad_mode
     if payload == "mode piano":
        drum_pad_mode = 'piano'
        print ("Mode set to " + drum_pad_mode)
     elif payload == "mode drums":
        drum_pad_mode = 'drums'
        print ("Mode set to " + drum_pad_mode)
     else:
        print "Message from Google Home: %s" % payload

def callback1(channel):
    if drum_pad_mode == 'default':
        print "Playing from port 24 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'piano':
        os.system('aplay -D bluealsa ~/Desktop/project/piano/a1.wav')
        print "Playing from port 24 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'drums':
	os.system('aplay -D bluealsa ~/Desktop/project/drums/tom.wav')
        print "Playing from port 24 in mode %s" % drum_pad_mode


def callback2(channel):
    if drum_pad_mode == 'default':
        print "Playing from port 23 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'piano':
        os.system('aplay -D bluealsa ~/Desktop/project/piano/b1.wav')
        print "Playing from port 23 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'drums':
        os.system('aplay -D bluealsa ~/Desktop/project/drums/snare.wav')
        print "Playing from port 23 in mode %s" % drum_pad_mode

def callback3(channel):
    if drum_pad_mode == 'default':
        print "Playing from port 18 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'piano':
        os.system('aplay -D bluealsa ~/Desktop/project/piano/c1.wav')
        print "Playing from port 18 in mode %s" % drum_pad_mode
    elif drum_pad_mode == 'drums':
        os.system('aplay -D bluealsa ~/Desktop/project/drums/hat.wav')
        print "Playing from port 18 in mode %s" % drum_pad_mode



# Function defenitions end hello

def main():
        client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
        client.on_connect    = connected
        client.on_message    = message
        client.connect()
        GPIO.add_event_detect(24, GPIO.BOTH, callback=callback1, bouncetime=500)
 	    GPIO.add_event_detect(18, GPIO.BOTH, callback=callback2, bouncetime=500)
        GPIO.add_event_detect(23, GPIO.BOTH, callback=callback3, bouncetime=500)
        client.loop_blocking()
        GPIO.cleanup()

if __name__ == "__main__":
        main()
