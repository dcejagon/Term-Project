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
import Encoder
import REncoder
import MotorDriver
import SingleMotorDriver
import ClosedLoop
import ThetaMotorControl
import RMotorControl
import ServoMotorF
import LimitSwitch
import pyb
import time

## MOTOR PIN STUFF
##Motor 1, Theta
en_pin=pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
in1pin=pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
in2pin=pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
timer=3

##Motor 2, R
en_pin2=pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
in1pin2=pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
in2pin2=pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
timer2=5


##ENCODER PIN STUFF
ENCpin1=pyb.Pin (pyb.Pin.board.PB6)
ENCpin2=pyb.Pin (pyb.Pin.board.PB7)
timernumber=4

ENC2pin1=pyb.Pin (pyb.Pin.board.PC6)
ENC2pin2=pyb.Pin (pyb.Pin.board.PC7)
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

Rswitch = task_share.Share ('h', thread_protect = False, name = "R_Switch")
Tswitch = task_share.Share ('h', thread_protect = False, name = "T_Switch")

setpoint1.put(-90)   #Theta Setpoint (Degrees)
setpoint2.put(-270)    #R setpoint (degrees)
xpos.put(4)
ypos.put(4)

Kp1.put(1)
Kp2.put(1)      #Motor A

##OBJECTS
motor1=MotorDriver.MotorDriver(en_pin, en_pin2, in1pin, in2pin, in1pin2, in2pin2, timer, timer2,duty1,duty2)
#motor1=SingleMotorDriver.MotorDriver(en_pin,in1pin,in2pin,timer,duty1)
motor2=MotorDriver.MotorDriver(en_pin, en_pin2, in1pin, in2pin, in1pin2, in2pin2, timer, timer2,duty1,duty2)

ENC1=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,ENC2pin1,ENC2pin2,timernumber,timernumber2,EncPosition,EncPosition2)
#ENC2=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,ENC2pin1,ENC2pin2,timernumber,timernumber2,EncPosition,EncPosition2)
ENC2=REncoder.EncoderDriver(ENC2pin1,ENC2pin2,timernumber2,EncPosition2)
ThEnc=Encoder.Encoder(ENCpin1,ENCpin2,timernumber)
#ThEnc2=EncoderDriver.EncoderDriver(ENCpin1,ENCpin2,ENC2pin1,ENC2pin2,timernumber,timernumber2,EncPosition1,EncPosition2)

# Cl1=ClosedLoop.ClosedLoop(Kp1,Kp2,setpoint1,setpoint2,EncPosition,EncPosition2,duty1,duty2,time)
# Cl2=ClosedLoop.ClosedLoop(Kp1,Kp2,setpoint1,setpoint2,EncPosition,EncPosition2,duty1,duty2,time)

ThetaControl=ThetaMotorControl.ThetaClosedLoop(Kp1,setpoint1,EncPosition,duty1,xpos,ypos)
RControl=RMotorControl.RClosedLoop(Kp2,setpoint2,EncPosition2,duty2,xpos,ypos)

# servopin = pyb.Pin (pyb.Pin.board.D6, pyb.Pin.OUT_PP)
# servotimer =2
# servoch = 3

# switchpin1=pyb.Pin(pyb.Pin.board.D7, pyb.Pin.IN, pyb.Pin.PULL_DOWN) #PB4
# switchpin2=pyb.Pin(pyb.Pin.board.D9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

# Servo=ServoMotorF.ServoMotorF(servopin, servotimer, servoch)
#LSwitch=LimitSwitch.LimitSwitch(switchpin1,switchpin2)

zpos.put(0)
def task1_fun ():
    '''!
        runs tasks and functions for the first motor
    '''
    while True:
        #Theta Direction
    # #do motor 1 stuff here       
        ENC1.read()
        ThetaControl.control_loop1()
        #not running thetamotorcontrol
        motor1.set_duty_cycle(duty1.get())
        
        yield (0)
        
def task2_fun ():
    while True:
        #R Direction
        ENC2.read()
        RControl.control_loop()
        motor2.set_duty_cycle2(duty2.get())
        
        yield(0)

def task3_fun():
    while True:        
        # LSwitch.checkswitch()
        
        yield (0)
        
# def task4_fun():
#     while True:
#         print ('servo') 
#         yield (0)



# def task4_fun():
#     while True:
#         print('servo')
#         # if zpos.get()==0:
#         #     Servo.up()
            
#         # elif zpos.get()==1:
#         #     Servo.down()
            
#         # else: 
#         #     pass
        
#         yield(0)
        
# def task4_fun ():
#     while True:
#         print('SWitchTask')
#         switchpin1.value()
#         LSwitch.checkswitch()
#         yield (0)

if __name__=="__main__":
    while True:
        try:
            x = int(input())
            while True: 
                try: 
                    if x <= 10:
                        task1 = cotask.Task (task1_fun, name = 'Task_1', priority = 2, 
                                             period = 10, profile = True, trace = False)
                        task2 = cotask.Task (task2_fun, name = 'Task_2', priority = 1, 
                                             period = 10, profile = True, trace = False)
                        task3 = cotask.Task (task3_fun, name = 'Task_3', priority = 1, 
                                            period = 40, profile = True, trace = False)
                        task3 = cotask.Task (task3_fun, name = 'Task_3', priority = 1, 
                                            period = 30, profile = True, trace = False)
                        # task4 = cotask.Task (task3_fun, name = 'Task_4', priority = 2, 
                        #                     period = 20, profile = True, trace = False)
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
                
