''' @file                       MotorDriver.py
    @brief                      A driver file for interacting with motors
    @details                    This driver file interacts with motors by sending duty cycle values and setting pin values to 
                                control the motor behavior.
                                
    @author                     Daniel Gonzalez
    @author                     Nolan Clapp
    @author                     Caleb Kephart
    @date                       January 24, 2022
'''
import pyb
class MotorDriver:
    ''' @brief                  This class implements a motor driver for an ME405 kit. 
        @details                Class composed of two functions to manipulate a motor.
    '''

    def __init__ (self,en_pin,en_pin2,in1pin,in2pin,in1pin2,in2pin2,timer,timer2,duty1,duty2):
        '''!
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin The enable pin for motor 1
        @param en_pin2 The enable pin for motor 2
        @param in1pin Pin 1 that the motor1 connects to on the Neucleo
        @param in2pin Pin 2 that the motor1 connects to on the Neucleo
        @param in1pin2 Pin 1 that the motor2 connects to on the Neucleo
        @param in2pin2 Pin 2 that the motor2 connects to on the Neucleo
        @param timer Timer number associated with motor1
        @param timer2 Timer number associated with motor2
        @param duty1 PWM% supplied to motor1
        @param duty2 PWM% supplied to motor2
        '''
        
        ## @brief Initializes pin to enable motor 1
        #
        self.en_pin=en_pin
        ## @brief Initializes pin to enable motor 2
        #
        self.en_pin2=en_pin2
        ## @brief Initializes In1 Pin
        #
        self.in1pin=in1pin
        ## @brief Initializes In2 Pin
        #
        self.in2pin=in2pin
        
        self.in1pin2=in1pin2
        ## @brief Initializes In2 Pin
        #
        self.in2pin2=in2pin2
        
        ## @brief Initializes timer for motor 1
        #
        self.timer=timer
        ## @brief Initializes timer for motor 2
        #
        self.timer2=timer2
        ## @brief Sets up motor timer 1
        #  @details This variable sets up motor timer 1 with a frequency of 20000hz
        self.tim3 = pyb.Timer (self.timer, freq=20000)
        ## @brief Sets motor channel and pins to recieve PWM
        #
        self.ch1 = self.tim3.channel (1, pyb.Timer.PWM, pin=in1pin)
        ## @brief Sets motor channel and pins to recieve PWM
        #
        self.ch2 = self.tim3.channel (2, pyb.Timer.PWM, pin=in2pin)

        ## @brief Sets up motor timer 2
        #  @details This variable sets up motor timer 2 with a frequency of 20000hz
        self.tim5 = pyb.Timer (self.timer2, freq=20000)
        ## @brief Sets motor channel and pins to recieve PWM
        #
        self.ch12 = self.tim5.channel (1, pyb.Timer.PWM, pin=in1pin2)
        ## @brief Sets motor channel and pins to recieve PWM
        #
        self.ch22 = self.tim5.channel (2, pyb.Timer.PWM, pin=in2pin2)
        
        ## @brief Sets up a variable for the duty to motor 1
        #  @details This variable sets up the Pulse Width Percent that 
        #           will be supplied to motor 1 to cause rotation. This variable
        #           is shared between files so we can calculate the value in 
        #           our closed loop controller. 
        self.duty1=duty1
        ## @brief Sets up a variable for the duty to motor 2
        #  @details This variable sets up the Pulse Width Percent that 
        #           will be supplied to motor 2 to cause rotation. This variable
        #           is shared between files so we can calculate the value in 
        #           our closed loop controller. 
        self.duty2=duty2
        print ('Creating a motor driver')

    def set_duty_cycle (self,duty1):
        '''
        @brief This function allows us to set a duty cycle for the motor 1
        @details This method sets the duty cycle to be sent
        to the motor at a given level. Positive values
        cause rotation in one direction, negative values
        in the opposite direction. We accomplish this rotation by using the 
        pulse_width_percent(#) method for each of our channels. By applying #
        to channel 1 and 0 to channel 2, the motor will rotate one way. By applying
        0 to channel 1 and # to channel 2, the motor will rotate the opposite way. 
        @param duty1 signed integer holding the duty
               cycle sent to the motor 
        '''
        
        
        self.en_pin.high()
        self.in1pin.low()
        self.in2pin.low()
          
        ## @brief Variable to temporarily hold duty value
        level=self.duty1.get()
        #print(self.duty1.get())
        if level>=0:
            
            
            self.ch1.pulse_width_percent(level)
            self.ch2.pulse_width_percent(0)
            #print('Theta Motor Working')
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(abs(level))
             
    def set_duty_cycle2(self,duty2): 
        #R MOTOR STUFF
        self.en_pin2.high()
        self.in1pin2.low()
        self.in2pin2.low()
        if self.duty2.get()>=0: 
            self.ch12.pulse_width_percent(self.duty2.get())
            self.ch22.pulse_width_percent(0)
        else:
            self.ch12.pulse_width_percent(0)
            self.ch22.pulse_width_percent(abs(self.duty2.get()))
        
        


if __name__=="__main__":
    import pyb
    en_pin=pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
    in1pin=pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    in2pin=pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
    timer=3
    motor1=MotorDriver(en_pin, in1pin, in2pin, timer)
    motor1.set_duty_cycle(50)
    
     