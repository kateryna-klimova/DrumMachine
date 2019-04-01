#!/usr/bin/env python

"""Main Script"""
# Working script
# Imports
from Adafruit_IO import MQTTClient
from time import sleep
import os
import os.path
import RPi.GPIO as GPIO
import os
import os.path
import multiprocessing

# Setting global variables
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ADAFRUIT_IO_USERNAME = "katerynaklimova"
ADAFRUIT_IO_KEY = "e2eee5f63ba54e26b3fb8bb70dd4bd09"

# Function definitions

# Subscribes to the Adafruit stream
def connected(client):
    client.subscribe('google_commands')

# this gets called every time a message is received hehbkh
def message(client, feed_id, payload):  # proces the commands from Google Home
     if payload == "mode piano" or payload == "mold piano":
        cmd.value = 1
        print("Mode set to piano")
     elif payload == "mode drums" or payload == "mold drums":
        cmd.value = 2
        print("Mode set to drums")
     elif payload == "mode beat" or payload == "mold beat":
       cmd.value = 3
       print("Mode set to beat")
     elif payload == "record":
        cmd.value = 4
        print("Recording started")
     elif payload == "stop recording":
        cmd.value = 5
        print("Recording stopped")
     else:
        print "Message from Google Home: %s" % payload


def callback1(channel):
    buttons[0] = 1

def callback2(channel):
    buttons[1] = 1

def callback3(channel):
    buttons[2] = 1

def callback4(channel):
    buttons[3] = 1

def callback5(channel):
    buttons[4] = 1

def callback6(channel):
    buttons[5] = 1

def callback7(channel):
    buttons[6] = 1

def callback8(channel):
    buttons[7] = 1

def callback9(channel):
    buttons[8] = 1

def func(cmd, buttons):
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    client.on_connect = connected
    client.on_message = message
    client.connect()
    client.loop_blocking()


# Function defenitions end

def func2(cmd, buttons):
    GPIO.add_event_detect(24, GPIO.BOTH, callback=callback1, bouncetime=50)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=callback2, bouncetime=50)
    GPIO.add_event_detect(23, GPIO.BOTH, callback=callback3, bouncetime=50)
    GPIO.add_event_detect(17, GPIO.BOTH, callback=callback4, bouncetime=50)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=callback5, bouncetime=50)
    GPIO.add_event_detect(22, GPIO.BOTH, callback=callback6, bouncetime=50)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=callback7, bouncetime=50)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=callback8, bouncetime=50)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=callback9, bouncetime=50)
    while True:
        if cmd.value == 1:
            if (buttons[0] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/a1.wav')
                buttons[0] = 0
            if (buttons[1] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/b1.wav')
                buttons[1] = 0
            if (buttons[2] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/c1.wav')
                buttons[2] = 0
            if (buttons[3] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/d1.wav')
                buttons[3] = 0
            if (buttons[4] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/e1.wav')
                buttons[4] = 0
            if (buttons[5] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/g1.wav')
                buttons[5] = 0
            if (buttons[6] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/f1.wav')
                buttons[6] = 0
            if (buttons[7] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/a1s.wav')
                buttons[7] = 0
            if (buttons[8] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/d1s.wav')
                buttons[8] = 0
        elif cmd.value == 2:
            if (buttons[0] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/tom.wav')
                buttons[0] = 0
            if (buttons[1] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/snare.wav')
                buttons[1] = 0
            if (buttons[2] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/hat.wav')
                buttons[2] = 0
            if (buttons[3] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/sharp_snare.wav')
                buttons[3] = 0
            if (buttons[4] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/snare_double.wav')
                buttons[4] = 0
            if (buttons[5] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/snare_edge.wav')
                buttons[5] = 0
            if (buttons[6] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/kick2.wav')
                buttons[6] = 0
            if (buttons[7] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/tom2.wav')
                buttons[7] = 0
            if (buttons[8] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/kick.wav')
                buttons[8] = 0

        elif cmd.value == 3:
            if (buttons[0] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/5.wav')
                buttons[0] = 0
            if (buttons[1] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/2.wav')
                buttons[1] = 0
            if (buttons[2] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/3.wav')
                buttons[2] = 0
            if (buttons[3] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/4.wav')
                buttons[3] = 0
            if (buttons[4] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/5.wav')
                buttons[4] = 0
            if (buttons[5] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/6.wav')
                buttons[5] = 0
            if (buttons[6] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/4.wav')
                buttons[6] = 0
            if (buttons[7] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/8.wav')
                buttons[7] = 0
            if (buttons[8] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/3.wav')
                buttons[8] = 0

        elif cmd.value == 0: #default
            if (buttons[0] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/8.wav')
                buttons[0] = 0
            if (buttons[1] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/snare.wav')
                buttons[1] = 0
            if (buttons[2] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/a1.wav')
                buttons[2] = 0
            if (buttons[3] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/e1.wav')
                buttons[3] = 0
            if (buttons[4] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/4.wav')
                buttons[4] = 0
            if (buttons[5] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/snare_edge.wav')
                buttons[5] = 0
            if (buttons[6] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/drums/kick2.wav')
                buttons[6] = 0
            if (buttons[7] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/piano/g1.wav')
                buttons[7] = 0
            if (buttons[8] == 1):
                os.system('aplay -D bluealsa ~/Desktop/project/synth/2.wav')
                buttons[8] = 0
    GPIO.cleanup()


if __name__ == "__main__":
    cmd = multiprocessing.Value('i', 0)
    buttons = multiprocessing.Array('i', 9)
    a = multiprocessing.Process(target=func2, args=(cmd, buttons))
    b = multiprocessing.Process(target=func, args=(cmd, buttons))
    a.start()
    b.start()
