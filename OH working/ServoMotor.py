# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:37:53 2022

@author: dceja
"""

import pyb 
import time

pinD6 = pyb.Pin (pyb.Pin.board.D6, pyb.Pin.OUT_PP)
tim2 = pyb.Timer (2, freq=50)
ch2 = tim2.channel (3, pyb.Timer.PWM, pin=pinD6)

# servo1 = PWM(pinC7, freq = 50)


state = 1

port = pyb.USB_VCP

#u_input = port(1).decode()

if __name__ == "__main__":
    
    while (True):
        try:
            
            if state == 1:
                ch2.pulse_width_percent(1) #10.75=90degees
                
                time.sleep(1)
                state=2
                
                print("Servo is Up")
            elif state == 2:
                ch2.pulse_width_percent(11) #10.75=90degees
                time.sleep(1)
                print("Servo is Down")
                state=1
        except KeyboardInterrupt:
            print("ERROR!")
            break
        