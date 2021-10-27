# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#RGB pins are initialized into output mode
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

def dot(red, green, blue):
    if(red):
        GPIO.output(LED_R, GPIO.HIGH)
    if(green):
        GPIO.output(LED_B, GPIO.HIGH)
    if(blue):
        GPIO.output(LED_G, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(0.5)

def dash(red, green, blue):
    if(red):
        GPIO.output(LED_R, GPIO.HIGH)
    if(green):
        GPIO.output(LED_B, GPIO.HIGH)
    if(blue):
        GPIO.output(LED_G, GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(0.5)

#Display LEDs
while True:
        #A ('.-') in red
        dot(True, False, False)
        dash(True, False, False)

        #D ('-..') in yellow
        dash(True, True, False)
        dot(True, True, False)
        dot(True, True, False)

        #Y ('-.--') in green
        dash(False, True, False)
        dot(False, True, False)
        dash(False, True, False)
        dash(False, True, False)

        #E ('.') in turquoise
        dot(False, True, True)

        #N ('-.') in blue
        dash(False, False, True)
        dot(False, False, True)

GPIO.cleanup()