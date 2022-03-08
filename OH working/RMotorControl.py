
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
import utime
import time
import math 
#from matplotlib import pyplot as plt

class RClosedLoop:
    ''' @brief Puts system into a closed loop.
        @details This code allows us to run the motor/encoder system within a closed loop.
    '''
    
    #def __init__(self,Kp2,setpoint2,EncPosition2,duty2,xpos,ypos):
    def __init__(self,Kp2,setpoint2,EncPosition2,duty2,RGO):
        ''' @brief          Constructs a closed loop object
            @details        Sets up the closed loop so that it can intake data from the encoder and main to send to the motor driver.
            @param Kp       This parameter allows us to choose the gain utilized by the system
            @param EncPosition  This parameter allows for the class to intake the encoder position data
            @param duty     This parameter chooses the duty cycle for the motor
            @param time     This parameter sets a timer to be used for the data collection
            
        '''
        ## @brief System Gain for motor 1
        #
        self.Kp2=Kp2 

        ## @brief Desired encoder position
        #
        self.setpoint2=setpoint2

        ## @brief Actual Encoder Position
        #  @details Allows for the class to read encoder position data from the 
        #           encoder.
        #
        self.EncPosition2=EncPosition2

        ## @brief sets duty cycle for motor
        #
        self.duty2=duty2
        
        ## @brief sets timer for data collection
        #
        self.RGO=RGO
        #
        #
        #
        # self.xpos=xpos
        
        # self.ypos=ypos
        #
        #
        #
        ## @brief array of time data
        #
        self.Time1=[]
        ## @brief array of actual position data
        #
        self.Pos1=[]
 
        ## @brief starting time of data collection 
        #
        self.starttime=time.ticks_ms()
        
    def Setpoint(self,setpoint1,setpoint2):
        '''!
            Accesses the setpoint shares to set final encoder position for each motor.
        '''
        self.setpoint1=setpoint1.get()

        
    def SetKp(self,Kp):
        '''!
            accesses Kp share 
        '''
        self.Kp=Kp.get()
        
            
    def control_loop(self):
        '''!
            funciton will put motor in a closed loop with the desired setpoint and gain.
        '''
        #Theta Direction
        #This calculates the correct setpoint based on shared x and y position values from GCode
        #R=math.sqrt(self.xpos.get()^2+self.ypos.get()^2)
        # Factor to convert from rotations (ticks) to linear position
        # 1 motor rotation= 1.51 inches in R direction
        #360 degrees = 4096*4 ticks (multiply desired degrees by 4096*4/360)
        #degtolin=4096*4/1.51
        #self.setpoint2.put(R*degtolin)
        ## @brief the error between actual and desired position
        #
        #print('Running Control Loop for R')
        self.error2=self.setpoint2.get()-self.EncPosition2.get()*360/(4096*4)
        if self.error2>=7:
            self.RGO.put(0)
        elif self.error2<7:
            self.RGO.put(1)
        print('R Error:',self.error2)
        ## @brief the duty cycle required for the system to correct with set gain.
        #print(self.error2)
        
        #print('R Encoder Position:',self.EncPosition2.get()*360/(4096*4))
        self.actuation2=self.Kp2.get()*self.error2
        #print(self.actuation2)
        self.duty2.put(self.actuation2)
        #print(self.duty2.get(),'=R Duty')
        
        # utime.sleep_ms(10)
        #print(time.ticks_ms(),self.EncPosition.get())
        
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
        

    
        
        
    
    
    
        

