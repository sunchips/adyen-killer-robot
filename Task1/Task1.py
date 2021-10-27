# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of LED module pins
LED_R = 22
LED_G = 27
LED_B = 24

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#LED pins are initialized into output mode
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

#Display LEDs
while True:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)

GPIO.cleanup()
