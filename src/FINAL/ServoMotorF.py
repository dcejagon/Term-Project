"""
    @file                    ServoMotor.py
    @brief                   This file for interacting with a servo motor and a kill switch
    @details                 This driver file interacts with servo motor by sending a PWM signal through a set pin.
                             The positioning of the servo motor is controlled by the PWM signal. 
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    Feburary 22, 2022
"""

import pyb 
import time
class ServoMotorF:
    ''' @brief               This class implements a driver to control a servo motor
        @details             Class is composed of two functions to control the servo's positioning
    '''
    def __init__(self,pin,timern,ch):
        '''
            @brief   Creates a servo driver by initializing pins
            @param   pin Pin A7 that the servo motor connects to on the Nucleo
            @param   timern Timer number associated with the servo motor
            @param   Channel number associated with the timer of servo motor
        '''
        ## @brief Variable for the pin our servo motor is connected to
        #  @details This variable sets up our servo motor pin as pin A7
        self.pinA7 = pin
        ## @brief Variable for the timer for our servo motor pin (timer 17)       
        self.timern=timern
        ## @brief Variable for the timer for our servo motor cahnnel (ch 1)
        self.ch = ch
        ## @brief Variable for the timer for our servo motor pin (timer 17)       
        self.tim17 = pyb.Timer (17, freq=75)
        ## @brief Instantiates ch1 for timer 17 for pwm
        self.ch1 = self.tim17.channel (1, pyb.Timer.PWM, pin=self.pinA7)
        
    def up(self):
        '''
            @brief     This function allows us to send a PWM signal to move servo up
            @details   This method sends a PWM signal to the servo motor which is
                       interpreted as a position, as the PWM % increases the pen moves up.
            @return    Returns value, 1, associated with up position.
        '''
        # PWM % of 1 is pointing down towards the sharpie tip, and increase to move the pen upwards
        self.ch1.pulse_width_percent(16)
        #print('Pen Raised')
        return 1
    def down(self):
        '''
            @brief     This function allows us to send a PWM signal to move servo down
            @details   This method sends a PWM signal to the servo motor which is
                       interpreted as a position, as the PWM % decreases the pen moves down. 
            @return    Returns value, 2, associated with down position.
        '''
        self.ch1.pulse_width_percent(7.5)
        #print('Pen Lowered')
        return 2
    
class LimitSwitch:
    ''' @brief               This class initializes a limit switch used on the R motor.
        @details             Class has a function which checks the value of the limit switch pin
    '''
    def __init__(self,switchpin1,switchpin2,duty2,Rswitch):
        '''
            @brief   Creates a limit swtich by initializing pins
            @param   switchpin1 This parameter allows us to select and check the value of the first pin of the limit switch 
            @param   switchpin2 This parameter allows us to choose the second pin our limit switch will be using 
            @param   duty2      This parameter chooses the duty cycle for the R motor
            @param   Rswitch    This parameter allows us store the limit switch pin value
        '''
        ## @brief Variable for the pin our first limit switch is connected to
        #  @details This variable sets up our servo motor pin as pin A8 and uses a 
        #           pull down resistor to ensure correct output.
        self.switchpin1=switchpin1
        ## @brief Variable for the pin our second limit switch is connected to
        #  @details This variable sets up our servo motor pin as pin A6 and uses a 
        #           pull down resistor to ensure correct output.
        self.switchpin2=switchpin2
        ## @brief Shared Variable for duty of motor 2
        #  @details This shared variable for the duty of motor 2 is set up to be 
        #           a float. This is important because when we write to this variable in 
        #           our closed loop controller, the number we calculate is a float. 
        self.duty2=duty2
        ## @brief Shared variable for the value of our R limit switch
        #  @details This variable contains the value of the pin that our limit switch is 
        #           connected to. We are using this limit switch as a kill switch so that
        #           when the pin value changes from 1 to 0, the duty to all our motors is 
        #           set to 0. This prevents our motors from burning up when the parts reach 
        #           a mechanical stop. 
        self.Rswitch=Rswitch
    print('initializing limit switch')
    def checkswitch(self):
        '''
            @brief   Checks the limitswitch value and determines if the duty needs to be set to zero.
            @details The function checks the value of the switchpin1
                     and if the value is 0 then it will set the duty for the R motor to zero.  
        '''
        
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
        