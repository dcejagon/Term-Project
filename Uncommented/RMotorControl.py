"""
    @file                    RMotorControl.py
    @brief                   This file provides the code to run closed loop control on R motor
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    March 8, 2022
"""
import utime
import time


class RClosedLoop:
    ''' @brief Puts system into a closed loop.
        @details This code allows us to run the motor/encoder system within a closed loop.
    '''
    
    def __init__(self,Kp2,setpoint2,EncPosition2,duty2,RGO):
        '''
            @brief          Constructs a closed loop object for R Motor
            @details        Sets up the closed loop so that it can intake data from the encoder and main to send to the motor driver.
            @param Kp2       This parameter allows us to choose the gain utilized by the system
            @param setpoint2    This parameter holds the desired motor position
            @param EncPosition2  This parameter allows for the class to intake the encoder position data
            @param duty2     This parameter chooses the duty cycle for the motor
            @param RGO   This parameter allows us to cycle through our FSM in main when we are within a desired range of our setpoint
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
        ## @brief array of time data
        #
        self.Time1=[]
        ## @brief array of actual position data
        #
        self.Pos1=[]
        ## @brief starting time of data collection 
        #
        self.starttime=time.ticks_ms()
        
            
    def control_loop(self):
        '''
            @brief Runs closed loop control on R motor
            @details This method runs the closed loop control system for the R motor. 
            we accomplish this by multiplying the difference between the setpoint and the 
            current position by a porportional gain. We then write this value to the duty
            that will be passed into our motor driver. 
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
        self.error2=self.setpoint2.get()-self.EncPosition2.get()*360/(4096*4)
        if abs(self.error2)>=5:
            self.RGO.put(0)
            
        elif abs(self.error2)<5:
            self.RGO.put(1)
            
       
        ## @brief the duty cycle required for the system to correct with set gain.
      
        self.actuation2=self.Kp2.get()*self.error2
        
        self.duty2.put(self.actuation2)
       
    

















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
        

    
        
        
    
    
    
        

