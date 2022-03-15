"""
    @file                    ServoMotor.py
    @brief                   This file for interacting with a servo motor
    @details                 This driver file interacts with servo motor by sending a PWM signal through a set pin.
                             The positioning of the servo motor is controlled by the PWM signal. 
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    Feburary 22, 2022
"""

import pyb 
import time

'''@brief   Defines servo motor pin, state variable and timer
'''

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
                '''@brief   Sends PWM signal to move Servo up'''
                ch2.pulse_width_percent(1) #10.75=90degees
                
                time.sleep(1)
                state=2
                
                print("Servo is Up")
            elif state == 2:
                '''@brief   Sends PWM signal to move Servo down'''
                ch2.pulse_width_percent(11) #10.75=90degees
                time.sleep(1)
                print("Servo is Down")
                state=1
        except KeyboardInterrupt:
            print("ERROR!")
            break
        