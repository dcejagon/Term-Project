"""
    @file                    ThetaMotorControl.py
    @brief                   This file provides the code to run closed loop control on Theta motor
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    March 8, 2022
"""
import utime
import time

class ThetaClosedLoop:
    ''' @brief Puts system into a closed loop.
        @details This code allows us to run the motor/encoder system within a closed loop.
        by calculating the actuation signal from the difference between the current 
        setpoint and current position multiplied by gain Kp1. 
    '''

    def __init__(self, Kp1, setpoint1, EncPosition1, duty1,THETAGO):
        ''' 
            @brief          Constructs a closed loop object for Theta Motor
            @details        Sets up the closed loop so that it can intake data from the encoder and main to send to the motor driver.
            @param Kp1       This parameter allows us to choose the gain utilized by the system
            @param setpoint1    This parameter holds the desired motor position
            @param EncPosition1  This parameter allows for the class to intake the encoder position data
            @param duty1     This parameter chooses the duty cycle for the motor
            @param THETAGO   This parameter allows us to cycle through our FSM in main when we are within a desired range of our setpoint

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
        # @brief array of time data
        #
        self.Time1 = []
        # @brief array of actual position data
        #
        self.Pos1 = []

        # @brief starting time of data collection
        #
        self.starttime = time.ticks_ms()


    def control_loop1(self):
        '''
            @brief Runs closed loop control on theta motor
            @details This method runs the closed loop control system for the theta motor. 
            we accomplish this by multiplying the difference between the setpoint and the 
            current position by a porportional gain. We then write this value to the duty
            that will be passed into our motor driver. 
        '''

        # Theta Direction
        # This calculates the correct setpoint based on shared x and y position values from GCode
        # 360 degrees = 4096*4 ticks (multiply desired degrees by 4096*4/360)
        # self.setpoint1.put(math.atan((self.ypos.get()/self.xpos.get())*180/math.pi)*16384/360)
        # print(self.setpoint1.get())
        # angle=self.setpoint1.get()*360/(4096*4)
        # print(angle)

        #r motor wont run unless theta go=true
        
        ## @brief the error between actual and desired position
        #  @detils Uses the encoder position in degrees and setpoint in degrees
        self.error1 = self.setpoint1.get()-self.EncPosition1.get()*360/(4096*4)
        if abs(self.error1)>=7 :
            print('OUTSIDE THETA RANGE')
            
            self.THETAGO.put(0)
        elif abs(self.error1)<7:
           # print('GETTING IN HERE')
            self.THETAGO.put(1)
        print('Theta Error:',self.error1)

        # @brief the duty cycle required for the system to correct with set gain.
        #
        self.actuation1 = self.Kp1.get()*self.error1

        self.duty1.put(self.actuation1)
