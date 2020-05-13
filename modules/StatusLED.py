#!/usr/bin//python3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)  #physical Pin-Nr.11 -> Indicator for CPU Usage under 33%
GPIO.setup(27, GPIO.OUT)  #physical Pin-Nr.13 -> Indicator for CPU Usage between 33% and 66%
GPIO.setup(22, GPIO.OUT)  #physical Pin-Nr.15 -> Indicator for CPU Usage above 66%
GPIO.setup(5, GPIO.OUT)   #physical Pin-Nr.33 -> Indicator for Fritzbox Online
GPIO.setup(6, GPIO.OUT)   #physical Pin-Nr.35 -> Indicator for PiHole Service Running
GPIO.setup(13, GPIO.OUT)  #physical Pin-Nr.37 -> Indicator for Host (HostChecker.py) online

def SystemLEDon():
    GPIO.output(18, GPIO.HIGH)
    
def CPU33LEDon():
    GPIO.output(17, GPIO.HIGH)
    
def CPU66LEDon():
    GPIO.output(27, GPIO.HIGH)
    
def CPU100LEDon():
    GPIO.output(22, GPIO.HIGH)
    
def FritzOnlineLEDon():
    GPIO.output(5, GPIO.HIGH)
    
def PiHoleLEDon():
    GPIO.output(6, GPIO.HIGH)
    
def HostLEDon():
    GPIO.output(13, GPIO.HIGH)
    
def SystemLEDoff():
    GPIO.output(18, GPIO.LOW)
    
def CPU33LEDoff():
    GPIO.output(17, GPIO.LOW)
    
def CPU66LEDoff():
    GPIO.output(27, GPIO.LOW)
    
def CPU100LEDoff():
    GPIO.output(22, GPIO.LOW)
    
def FritzOnlineLEDoff():
    GPIO.output(5, GPIO.LOW)
    
def PiHoleLEDoff():
    GPIO.output(6, GPIO.LOW)
    
def HostLEDoff():
    GPIO.output(13, GPIO.LOW)