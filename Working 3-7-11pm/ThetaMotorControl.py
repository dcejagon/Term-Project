# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:23:40 2022

@author: nclap
"""

"""
    @file                    ClosedLoop.py
    @brief                   This file provides the code to interface directly with the encoder hardware
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    January 31, 2022
"""
#from matplotlib import pyplot as plt




import utime
import time

class ThetaClosedLoop:
    ''' @brief Puts system into a closed loop.
        @details This code allows us to run the motor/encoder system within a closed loop.
    '''

    #def __init__(self, Kp1, setpoint1, EncPosition1, duty1, xpos, ypos):
    def __init__(self, Kp1, setpoint1, EncPosition1, duty1,THETAGO):
        ''' @brief          Constructs a closed loop object
            @details        Sets up the closed loop so that it can intake data from the encoder and main to send to the motor driver.
            @param Kp       This parameter allows us to choose the gain utilized by the system
            @param EncPosition  This parameter allows for the class to intake the encoder position data
            @param duty     This parameter chooses the duty cycle for the motor
            @param time     This parameter sets a timer to be used for the data collection

        '''
        # @brief System Gain for motor 1
        #
        self.Kp1 = Kp1

        # @brief Desired encoder position
        #
        self.setpoint1 = setpoint1

        # @brief Actual Encoder Position
        #  @details Allows for the class to read encoder position data from the
        #           encoder.
        #
        self.EncPosition1 = EncPosition1

        # @brief sets duty cycle for motor
        #
        self.duty1 = duty1

        # @brief sets timer for data collection
        #
        self.THETAGO=THETAGO
        #
        #
        #
        # self.xpos = xpos

        # self.ypos = ypos
        #
        #
        #
        # @brief array of time data
        #
        self.Time1 = []
        # @brief array of actual position data
        #
        self.Pos1 = []

        # @brief starting time of data collection
        #
        self.starttime = time.ticks_ms()

    def Setpoint(self, setpoint1, setpoint2):
        '''!
            Accesses the setpoint shares to set final encoder position for each motor.
        '''
        self.setpoint1 = setpoint1.get()

    def SetKp(self, Kp):
        '''!
            accesses Kp share 
        '''
        self.Kp = Kp.get()

    def control_loop1(self):
        '''!
            funciton will put motor in a closed loop with the desired setpoint and gain.
        '''

        # Theta Direction
        # This calculates the correct setpoint based on shared x and y position values from GCode
        # 360 degrees = 4096*4 ticks (multiply desired degrees by 4096*4/360)
        # self.setpoint1.put(math.atan((self.ypos.get()/self.xpos.get())*180/math.pi)*16384/360)
        # print(self.setpoint1.get())
        # angle=self.setpoint1.get()*360/(4096*4)
        # print(angle)

        #r motor wont run unless theta go=true
        # @brief the error between actual and desired position
        # @detils Uses the encoder position in degrees and setpoint in degrees
        self.error1 = self.setpoint1.get()-self.EncPosition1.get()*360/(4096*4)
        if abs(self.error1)>=3 :
            print('OUTSIDE THETA RANGE')
            
            self.THETAGO.put(0)
        elif abs(self.error1)<3:
           # print('GETTING IN HERE')
            self.THETAGO.put(1)
        #print('Theta Error:',self.error1)
        #print('Theta Duty:',self.duty1.get())
        #print(self.error1)
        #print('Theta Encoder:',self.EncPosition1.get()*360/(4096*4))
        # @brief the duty cycle required for the system to correct with set gain.
        #
        #print(self.error1)
        self.actuation1 = self.Kp1.get()*self.error1
        #print(self.actuation1)
        
        self.duty1.put(self.actuation1)
        #CONTROLS MOTOR A
        #print(self.duty1.get(), '=Theta Duty')
        #print(self.duty1.get())
        # utime.sleep_ms(10)
        # print(time.ticks_ms(),self.EncPosition.get())

        # self.Time1.append(time.ticks_diff(time.ticks_ms(),self.starttime))
        # self.Pos1.append(self.EncPosition1.get())

    # def printdata(self):
    #     '''!
    #         displays lists for time and encoder position while the task runs
    #     '''
    #     ## @brief index of arrays
    #     #
    #     n=0
    #     while n< len(self.Time1):
    #         print(self.Time1[n],',',self.Pos1[n])
    #         n=n+1
