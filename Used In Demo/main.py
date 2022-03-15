"""
    @file                    main.py
    @author                  Daniel Gonzalez
    @author                  Nolan Clapp
    @author                  Caleb Kephart
    @date                    February 7, 2022
"""

import gc
import pyb
import cotask
import task_share
import EncoderDriver
import REncoder
import MotorDriver
import ThetaMotorControl
import RMotorControl
import ServoMotorF
import pyb
import time

# MOTOR PIN STUFF
#Motor 1, Theta
## @brief This variable is for the enable pin for motor 1
#  @details This variable is responsible for holding the pin information for the pin that 
#           will enable motor 1 when it is set to high. The pin is Pin A10. 
en_pin=pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
## @brief This variable is for the first pin of motor 1
#  @details This variable is set to Pin B4, the first pin on the Neucleo for motor 1.
#           This pin is set as an output. 
in1pin=pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
## @brief This variable is for the second pin of motor 1
#  @details This variable is set to Pin B5, the first pin on the Neucleo for motor 1.
#           This pin is set as an output. 
in2pin=pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
## @brief This variable is for the timer number associated with motor 1
timer=3

#Motor 2, R
## @brief This variable is for the enable pin for motor 2
#  @details This variable is responsible for holding the pin information for the pin that 
#           will enable motor 2 when it is set to high. The pin is Pin C1. 
en_pin2=pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
## @brief This variable is for the first pin of motor 2
#  @details This variable is set to Pin A0, the first pin on the Neucleo for motor 2.
#           This pin is set as an output. 
in1pin2=pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
## @brief This variable is for the second pin of motor 2
#  @details This variable is set to Pin A1, the first pin on the Neucleo for motor 2.
#           This pin is set as an output. 
in2pin2=pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
## @brief This variable is for the timer number associated with motor 2
timer2=5


#ENCODER PIN STUFF
## @brief This variable is for the frist encoder pin of encoder 1
#  @details This variable sets up the first pin of encoder 1 as Pin B6
ENCpin1=pyb.Pin (pyb.Pin.board.PB6)
## @brief This variable is for the second encoder pin of encoder 1
#  @details This variable sets up the second pin of encoder 1 as Pin B7
ENCpin2=pyb.Pin (pyb.Pin.board.PB7)
## @brief This variable is for the timer number associated with encoder 1
timernumber=4

## @brief This variable is for the frist encoder pin of encoder 2
#  @details This variable sets up the first pin of encoder 2 as Pin BC6
ENC2pin1=pyb.Pin (pyb.Pin.board.PC6)
## @brief This variable is for the second encoder pin of encoder 2
#  @details This variable sets up the second pin of encoder 2 as Pin BC7
ENC2pin2=pyb.Pin (pyb.Pin.board.PC7)
## @brief This variable is for the timer number associated with encoder 2
timernumber2=8

## SHARES
duty1 = task_share.Share ('f', thread_protect = False, name = "Duty_1")
duty2 = task_share.Share ('f', thread_protect = False, name = "Duty_2")
EncPosition = task_share.Share ('h', thread_protect = False, name = "Position_1")
EncPosition2 = task_share.Share ('h', thread_protect = False, name = "Position_2")
Kp1 = task_share.Share ('f', thread_protect = False, name = "Porportional_Gain1")
Kp2 = task_share.Share ('f', thread_protect = False, name = "Porportional_Gain2")
setpoint1 = task_share.Share ('f', thread_protect = False, name = "Set_Point1")
setpoint2 = task_share.Share ('f', thread_protect = False, name = "Set_Point2")

xpos = task_share.Share ('h', thread_protect = False, name = "X_Position")
ypos = task_share.Share ('h', thread_protect = False, name = "Y_Position")
zpos = task_share.Share ('h', thread_protect = False, name = "z_Position")

THETAGO=task_share.Share ('h', thread_protect = False, name = "THETAGO")
RGO= task_share.Share ('h', thread_protect = False, name = "RGO")

Rswitch = task_share.Share ('h', thread_protect = False, name = "R_Switch")
Tswitch = task_share.Share ('h', thread_protect = False, name = "T_Switch")




Theta= task_share.Share ('f', thread_protect = False, name = "Theta")
R= task_share.Share ('f', thread_protect = False, name = "R")

setpoint1.put(0)     #Theta Setpoint (Degrees)
setpoint2.put(0)    #R setpoint (degrees) #Limit of 715


#Kp1.put(27)     #Theta Motor
Kp1.put(20)
#Kp2.put(7)      #R Motor
Kp2.put(10)
##OBJECTS
motor1=MotorDriver.MotorDriver(en_pin, en_pin2, in1pin, in2pin, in1pin2, in2pin2, timer, timer2,duty1,duty2)

motor2=MotorDriver.MotorDriver(en_pin, en_pin2, in1pin, in2pin, in1pin2, in2pin2, timer, timer2,duty1,duty2)

ENC1=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,ENC2pin1,ENC2pin2,timernumber,timernumber2,EncPosition,EncPosition2)

ENC2=REncoder.EncoderDriver(ENC2pin1,ENC2pin2,timernumber2,EncPosition2)

ThetaControl=ThetaMotorControl.ThetaClosedLoop(Kp1,setpoint1,EncPosition,duty1,THETAGO)
RControl=RMotorControl.RClosedLoop(Kp2,setpoint2,EncPosition2,duty2,RGO)

servopin = pyb.Pin (pyb.Pin.board.PA7, pyb.Pin.OUT_PP)
servotimer =17
servoch = 1

switchpin1=pyb.Pin(pyb.Pin.board.PA8, pyb.Pin.IN, pyb.Pin.PULL_DOWN) #PB4
switchpin2=pyb.Pin(pyb.Pin.board.PA6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

Servo=ServoMotorF.ServoMotorF(servopin, servotimer, servoch)
LSwitch=ServoMotorF.LimitSwitch(switchpin1,switchpin2,duty2,Rswitch)

zpos.put(0)
#up is 0
#down is 1

THETAGO.put(1)
RGO.put(1)
def task1_fun ():
    '''!
        runs tasks and functions for the first motor
    '''
    
    print('Task1')
    with open('RTest.txt') as R, open('TTest.txt') as T: #draws rectangle
    #with open('RTest.txt') as R, open('TTest.txt') as T:    #draws CP Logo ish
        print('Opened Both Files Successfully')
        while True:
            #time.sleep(1)
            if THETAGO.get()==1:
                r=R.readline()
                print('r=',r)
                setpoint2.put(float(r)*2) #Mult by 2 for CP Divide for Rect
                THETAGO.put(0)
            elif THETAGO.get()==0:
                print('Not Moving R')  
                yield(0)
                
            if RGO.get()==1:
                #print('Theta Motor Working')
                t=T.readline()
                print('t=',t)
                setpoint1.put(float(t)*2)   #Mult by 2 for CP Divide for Rect
                RGO.put(0)
            elif THETAGO.get()==0:
                print('Not Moving Theta')
                yield(0)
            yield(0)
            
def task2_fun ():
    
         
        while True:
                print('Running Control Loop')
                
                ENC2.read()
                RControl.control_loop()
                motor2.set_duty_cycle2(duty2.get())
            
                ENC1.read()
                ThetaControl.control_loop1()
                motor1.set_duty_cycle(duty1.get())
                if LSwitch.checkswitch()==0:
                    motor2.set_duty_cycle2(0)
                    pass
                

                yield(0) 
def task3_fun():
    
    print('Task3')
    while True:  
        # LSwitch.checkswitch()
        LSwitch.checkswitch()  
        if zpos.get()==0:
            Servo.up()
            
        elif zpos.get()==1:
            Servo.down()  
        else: 
            pass
        yield (0)
        

if __name__=="__main__":
    while True:
        try:
            x = int(input())
            while True: 
                try: 
                    if x <= 10:
                        task1 = cotask.Task (task1_fun, name = 'Task_1', priority = 2, 
                                             period = 200, profile = True, trace = False)
                        task2 = cotask.Task (task2_fun, name = 'Task_2', priority = 3, 
                                             period = 10, profile = True, trace = False)
                        task3 = cotask.Task (task3_fun, name = 'Task_3', priority = 2, 
                                            period = 40, profile = True, trace = False)
                        
                        # task4 = cotask.Task (task3_fun, name = 'Task_4', priority = 3, 
                        #                      period = 20, profile = True, trace = False)
                        cotask.task_list.append (task1)
                        cotask.task_list.append (task2)
                        cotask.task_list.append (task3)
                        # cotask.task_list.append (task4)
                    
                        # Run the memory garbage collector to ensure memory is as defragmented as
                        # possible before the real-time scheduler is started
                        gc.collect ()
                    
                        # Run the scheduler with the chosen scheduling algorithm. Quit if any 
                        # character is received through the serial port
                        vcp = pyb.USB_VCP ()
                        while not vcp.any ():
                            cotask.task_list.pri_sched ()
                    
                        # Empty the comm port buffer of the character(s) just pressed
                        vcp.read ()
                        
                except KeyboardInterrupt:
                    break
        except :
            break
                
