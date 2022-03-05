# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:37:53 2022

@author: dceja
"""

import pyb 
import time
class ServoMotorF:
    def __init__(self,pin,timern,ch):
        self.pinD6 = pin
        # self.tim2 = timer
        self.ch = ch
        self.timern=timern
        
        self.tim2 = pyb.Timer (2, freq=75)
        self.ch3 = self.tim2.channel (3, pyb.Timer.PWM, pin=self.pinD6)
    def up(self):
        # PWM % of 1 is pointing down towards the sharpie tip, and increase to move the pen upwards
        self.ch3.pulse_width_percent(16)
        print('Pen Raised')
    def down(self):
        self.ch3.pulse_width_percent(10)
        print('Pen Lowered')
    
if __name__ == "__main__":
    pinD6 = pyb.Pin (pyb.Pin.board.D6, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=75)
    ch3 = tim2.channel (3, pyb.Timer.PWM, pin=pinD6)
    Servo1=ServoMotorF(pinD6,tim2,ch3)
    
    #LIMIT SWITCH STUFF#
    pinD5=pyb.Pin(pyb.Pin.board.D5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
    pinD5.value()
    #Checks for high and low, high(1) is unpressed and low(0) is pressed
    
    while (True):
        try:
            Servo1.up()
            time.sleep (1)
            Servo1.down()
            time.sleep(1)
        except KeyboardInterrupt:
            print("ERROR!")
            break
        