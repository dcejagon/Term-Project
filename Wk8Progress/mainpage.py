'''
@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 

@mainpage

@section sec_intro   ME 405 Term Project Software Description
                        This is our project main page for the ME 405 plotter project, and the progress
                        we have made up to this point on the software side of the project. 
                        
                        Our Source Code Repository can be found:  \htmlonly <a href="https://github.com/dcejagon/Term-Project/tree/main/src">HERE</a> \endhtmlonly

@section sec_lb1     Task Diagram and File Structure 
   
We developed the Task Diagram seen below to demonstrate the file structure that we plan to use in our 2.5D plotter. 
Each of the files will have some combination of shares and/or queues in order to allow for variable 
data to be shared between files. The exact shares between files is shown in the diagram.
We will utilize this by using the Task_Shares.py file
that we have been provided to ensure the shared variables are set up correctly, and contain usable data. 
In addition, we plan to have the differnet tasks communicate with eachother using 
the structure outlined in previous labs and by using CoTasks.py to make sure we 
are taking advantage of cooperative multitasking.  To simplify what is going on in 
each of our files, we are only using FSMs at the task level. We have one for task2
MotorControl Task and task3 ServoMotor Task. These diagrams are shown in 
ThetaMotorControl.py and RMotorControl.py and ServoMotorF.py sections respectively. 

The files that we are using: \n
main.py- Main file that runs all of our tasks and instantiates all objects \n
EncoderDriver.py- Read the position of the Theta Motor \n
Encoder.py- Read the position of the R Motor \n
MotorDriver.py- Control the motor by supplying a duty \n
ThetaMotorControl.py- Closed loop control of Theta Motor \n
RMotorControl.py- Closed loop control of R Motor    \n
ServoMotorF.py- Control the servo motor responsible for our half axis as well as limit switch reading  \n
GcodeInterpreter.py- Writed R and Theta Setpoints to .txt file to be read later \n
   

The Task Diagram showing how these files are used is shown below. 


\image html OverallTaskDiagram.png "Overall Task Diagram "  width=900px  

\image html SubTaskDiagram.png "Sub-Task Diagram"  width=900px 


The frist image shows the Overall Task Diagram that is running in our system, and the second
shows the subtasks that are running inside of each task. We are running 3 tasks,
each represented by a different color box, Blue is task1, Red is task2, and Green is
task3. If there are multiple boxes of the same color, they are treated as subtasks.
Each of this subtasks and their shares is shown in the second picture. 
Each of the shares we are using is represented with a dashed line pointing from where
the variable is written to where the variable is read. We chose to split the task diagram
up this way so that it better demonstrated what is happening with each share.


The procedure on how we used our code is shown below:
    1. Create GCODE using http://jscut.org/jscut.html# by converting a .SVG to tool paths
    2. Save the .gcode file that was created as NAME.txt 
    3. Run  NAME.text through GcodeInterpreter.py to output text files for desired R and Theta motor angles
    4. Save all necessary files on the Nucleo
    5. Run main.py on the Nucleo to use the plotter \n  
        a. main.py uses cotask.py for cooperative multitasking. \n
        b. Task1 generates the setpoint for both motors \n
        c. Task2 calculates encoder position, runs closed loop controller, and runs motor driver with duty from the controller \n
        d. Task3 controls the servo motor. If we want to draw, Zpos=1, if we want to lift, Zpos=0 \n
        e. Repeat running all tasks until the ends of the setpoint text files are reached \n

 
    
@section sec_lb2    main.py   
This file is the starting point of all of our software. We set up all needed hardware to software interface
(pins and timers), set up our shared variables, and instantiate all objects. 
This file also contains the generator responsibile for running all of our tsaks 
cooperatively. 

@section sec_lb3    EncoderDriver.py and Encoder.py      

These two files are very similar, the only differnece is that EncoderDriver.py reads the Theta encoder
and Encoder.py reads only the R encoder. These files are only used to calculate encoder position. When
we read the encoder position, we write that value to a shared variable for each position. 
For example: ThetaEncoderPosition.write(EncoderPosition). We calcualte this encoder position
by calculating the encoder delta from a timer on the microcontroller and the previous time. 
This allows us to calculate encoder position without worrying about the encoder "overflowing,"
where the encoder position essentially resets to 0 once the reading reaches 65535. 
We decided to split EncoderDriver.py and Encoder.py to make it easy to troubleshoot any errors that 
may come up. Origionally, EncoderDriver.py was responsible for reading both encoder positions,
so that is why it has R encoder pins, timer, and shares passed into the class, but they are never used. 
Similarly, since we only need R motor stuff passed into Encoder, we changed that file to only have 
necessary values shared to that file. In short, instead of changing EncoderDriver.py from its origional
state, we left it as is, and created a single copy that would only be used for the R motor and deleted 
all information related to the Theta motor. 

@section sec_lb4    MotorDriver.py
This file is responsible for taking the duty input from other files and making the 
motors turn at that duty. Once the motor driver is instantiated, the methodd that are
called repeatidly are set_duty_cycle and set_duty_cycle2 (one for R motor and 1 for Theta motor).
These methods enable the motor by setting the enable pin to high, and also sets both
output pins to low. We then set the duty by changing the PWM % to the desired duty value.
If the desired duty is positive, we set the PWM duty cycle of channel1, but if it is negative,
e set the PWM duty cycle of channel2. The pin that does not have the duty cycle applied to it
is set to a duty of 0. 
Example: (Positive duty-> CH1.pule_width_percent(DUTY) and CH2.pule_width_percent(0))

@section sec_lb5    ThetaMotorControl.py and RMotorControl.py
These two files are responsible for all of our closed loop system control. We are using 
a simple porportional controller with gain Kp. The control loop that is run over and over
calculated the error signal (error=setpoint-EncoderPosition), multiplies that by gain, Kp,
and then sets the duty to this value, called the actuation signal. This file is necessary
to determine when our motor reaches the desired position. In addition, these files determine
when motor position gets within an acceptable range. Once this happens, we set a buffer variable
to true so that our code konws when it should generate a new setpoint. 

The FSM for the Motor Tasks (including EncoderDriver.py, Control Loops, and MotorDriver.py)
is shown below. 
\image html MotorControlFSM.png "FSMs for Motor Control Task" width=900px   

@section sec_lb6    ServoMotorF.py
This file is responsible for controling our servo motor and limit switch. We have classes
for both the servo motor, and the limit switch. The servo motor class contains methods
to raise and lower the servo motor called up() and down(). These methods are called in 
main when a certain Zpos variable changes value. For example, when Zpos=1, the servo motor
will move down. 

The limit switch class is responsible for reading the value output by the limit switch 
pins. This is done in the method checkswitch(). This checks the value of the pin
using the .value call for the pin. Since the switch was wired to be normally closed,
when there is nothing pressing the switch, pin.value()=1, but when it is pressed, 
pin.value()=0. We are using this limit switch as a kill switch, so when the value 
of the pin is 0, we set the duty of the R motor to 0 to prevent the hardware from
tearing itself apart. 

The FSM for this file is shown below
\image html ServoFSM.png "FSMs for Servo Motor" width=900px   

@section sec_lb7    GcodeInterpreter.py
In order to generate the path that the pen should take, we used http://jscut.org/jscut.html# ,
a website that accepts SVG images and converts it to GCODE. This website was nice, because 
each of the GCODE lines were G1, which is the call for a straight line. The GCODE that 
this website outputs is a series of straight lines that are very short (around 0.001"). 
This means, we essentially have a list of X-Y coordinates that trace out our image. 

We then use the file GcodeInterpreter.py, to take each line of GCODE, pull out the 
desired X-Y coordinates, and then preform some math to convert these to R-Theta
coordinates. From these R-Theta coordinates, we use our known gear ratios to write
the desired R Motor angle and Theta Motor angle to their own .txt files. 

We then read each line of these files in main.py to get the setpoint of both motors. 
This is only done when the motor has reached its previous setpoint and the buffer 
variable is set to 1. 





@author              Nolan Clapp
@author              Caleb Kephart
@author              Daniel Gonzalez
@date                Feb 22, 2022
'''