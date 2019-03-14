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
from multiprocessing import Process, Value, Lock

# Setting global variables
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# drum_pad_mode = 'piano'
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
record_tag = 0
ADAFRUIT_IO_USERNAME = "katerynaklimova"
ADAFRUIT_IO_KEY = "e2eee5f63ba54e26b3fb8bb70dd4bd09"

# Function definitions

# Subscribes to the Adafruit stream
def connected(client):
    client.subscribe('google_commands')

# this gets called every time a message is received hehbkh
def message(client, feed_id, payload):  # proces the commands from Google Home
     if payload == "mode piano":
        drum_pad_mode = 1
        print("Mode set to " + drum_pad_mode)
     elif payload == "mode drums":
        drum_pad_mode = 2
        print("Mode set to " + drum_pad_mode)
     elif payload == "record":
        record_tag = 1
        print("Recording started")
     elif payload == "stop recording":
        record_tag = 0
        print("Recording stopped")
     else:
        print "Message from Google Home: %s" % payload


def callback1(channel):
    global b1
    # if drum_pad_mode == 'default':
    #     print "Playing from port 24 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'piano':
    #     os.system('aplay -D bluealsa ~/Desktop/project/piano/a1.wav')
    #     print "Playing from port 24 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'drums':
    # os.system('aplay -D bluealsa ~/Desktop/project/drums/tom.wav')
    #     print "Playing from port 24 in mode %s" % drum_pad_mode
    b1 = 1


def callback2(channel):
    global b2
    # if drum_pad_mode == 'default':
    #     print "Playing from port 23 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'piano':
    #     os.system('aplay -D bluealsa ~/Desktop/project/piano/b1.wav')
    #     print "Playing from port 23 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'drums':
    #     os.system('aplay -D bluealsa ~/Desktop/project/drums/snare.wav')
    #     print "Playing from port 23 in mode %s" % drum_pad_mode
    b2 = 1


def callback3(channel):
    global b3
    # if drum_pad_mode == 'default':
    #     print "Playing from port 18 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'piano':
    #     os.system('aplay -D bluealsa ~/Desktop/project/piano/c1.wav')
    #     print "Playing from port 18 in mode %s" % drum_pad_mode
    # elif drum_pad_mode == 'drums':
    #     os.system('aplay -D bluealsa ~/Desktop/project/drums/hat.wav')
    #     print "Playing from port 18 in mode %s" % drum_pad_mode
    b3 = 1

def func(drum_pad_mode):
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    client.on_connect = connected
    client.on_message = message
    client.connect()
    client.loop_blocking()


# Function defenitions end

def func2(drum_pad_mode):
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    # global record_tag
    # global drum_pad_mode
    GPIO.add_event_detect(24, GPIO.BOTH, callback=callback1, bouncetime=500)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=callback2, bouncetime=500)
    GPIO.add_event_detect(23, GPIO.BOTH, callback=callback3, bouncetime=500)
    while True:
        # sleep(0.5)
        if drum_pad_mode == 1:
            if (b1 == 1):
                print "Playing b1 in mode piano"
                b1 = 0
            if (b2 == 1):
                print "Playing b2 in mode piano"
                b2 = 0
            if (b3 == 1):
                print "Playing b3 in mode piano"
                b3 = 0
        elif drum_pad_mode == 2:
            if (b1 == 1):
                print "Playing b1 in mode drums"
                b1 = 0
            if (b2 == 1):
                print "Playing b2 in mode drums"
                b2 = 0
            if (b3 == 1):
                print "Playing b3 in mode drums"
                b3 = 0
        elif drum_pad_mode == 0:
            if (b1 == 1):
                print "Playing b1 in mode default"
                b1 = 0
            if (b2 == 1):
                print "Playing b2 in mode default"
                b2 = 0
            if (b3 == 1):
                print "Playing b3 in mode default"
                b3 = 0
    GPIO.cleanup()


if __name__ == "__main__":
         # main()
    drum_pad_mode = Value('i', 0)
    Process(target=func2, args=(drum_pad_mode))
    Process(target=func, args=(drum_pad_mode))
