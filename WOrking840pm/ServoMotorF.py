# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:37:53 2022

@author: dceja
"""

import pyb 
import time
class ServoMotorF:
    def __init__(self,pin,timern,ch):
        self.pinA7 = pin
        # self.tim2 = timer
        self.ch = ch
        self.timern=timern
        
        self.tim17 = pyb.Timer (17, freq=75)
        self.ch1 = self.tim17.channel (1, pyb.Timer.PWM, pin=self.pinA7)
        
    def up(self):
        # PWM % of 1 is pointing down towards the sharpie tip, and increase to move the pen upwards
        self.ch1.pulse_width_percent(16)
        #print('Pen Raised')
        return 1
    def down(self):
        self.ch1.pulse_width_percent(7)
        #print('Pen Lowered')
        return 2
    
class LimitSwitch:
    
    def __init__(self,switchpin1,switchpin2,duty2,Rswitch):
        self.switchpin1=switchpin1
        self.switchpin2=switchpin2
        self.duty2=duty2
        self.Rswitch=Rswitch
    print('initializing limit switch')
    def checkswitch(self):
        #print('CHECKING SWITCH')
        #R=self.switch_pin1.value()
        #T=self.switch_pin2.value()
        
        if self.switchpin1.value()==1:
            #print('val=1')
            self.Rswitch.put(self.switchpin1.value())
            #print(self.Rswitch.get())
        elif self.switchpin1.value()==0:
            #print('val=2')
            self.Rswitch.put(self.switchpin1.value())
            self.duty2.put(0)
            print(self.Rswitch.get())
            
if __name__ == "__main__":
    # pinD6 = pyb.Pin (pyb.Pin.board.D6, pyb.Pin.OUT_PP)
    # tim2 = pyb.Timer (2, freq=75)
    # ch3 = tim2.channel (3, pyb.Timer.PWM, pin=pinD6)
    # Servo1=ServoMotorF(pinD6,tim2,ch3)
    
    #LIMIT SWITCH STUFF#
    pinA8=pyb.Pin(pyb.Pin.board.PA8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
    pinA8.value()
    #Checks for high and low, high(1) is unpressed and low(0) is pressed
    
    while (True):
        try:
            print('Limit Switch Value is:', pinA8.value())
            # Servo1.up()
            time.sleep (.5)
            # Servo1.down()
            
        except KeyboardInterrupt:
            print("ERROR!")
            break
        