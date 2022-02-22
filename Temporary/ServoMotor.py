# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:37:53 2022

@author: dceja
"""
from machine import PWM
import pyb 

pinC7 = pyb.Pin (pyb.Pin.board.PC7)

servo1 = PWM(pinC7, freq = 50)

state = 0

port = pyb.USB_VCP

#u_input = port(1).decode()

if __name__ == "__main__":
    
    while (True):
        try:
            state = 0
            if (port.any()):
                u_input = port(1).decode()
                if u_input ==('w'):
                   state = 1
                elif u_input ==('s'):
                   state = 2
                   
            if state == 1:
                servo1.duty(20)
                print("Servo is Up")
            elif state == 2:
                servo1.duty(120)
                print("Servo is Down")
        except KeyboardInterrupt:
            print("ERROR!")
            break
        