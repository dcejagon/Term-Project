# Term Project Report 
### Description 
For our term project, have designed a 2.5 axis plotter. This plotter will have 
a rotating arm with a carriage that extends out on the arm. The plotter will move
in both the R and Theta directions to achieve the plotting of an image. 
arm, with the actual pen extending out on the arm. The base of the plotter will 
hold 2 motors; the first motor will control the rotation of the arm similar to 
the motion of  a windshield wiper (Theta), while the second motor will change the radial 
position of the pen carrier(R). The radial motor will control the pen location by 
moving the sharpie carriage using belts driven by pulleys. The pen carriage will have a servo motor 
that controls the up and down motion of the pen (0.5 Axis). This plotter will 
convert an image to X-Y Gcode, and then we will convert that into cylindrical, 
R-Theta, coordinats due to our system being inheriently non-rectilinear. 
In addition, This plotter should berelatively low cost ~$15 per person. 
We intend to use materials commonly used in 3D printing like Aluminum T-Slot 
extrusion and V-Slot bearings. The full bill of materials and cost breakdown 
is seen below. Items that have a "-" in the cost column are parts that we have 
access to with no cost. Our main source for parts will be Amazon to eliminate 
shipping costs. Team members have access to 3D printers, which will be used 
to fabricate custom parts such as mounting brackets, main Sharpie carriage, 
and motor mounts at no additional cost.  
### Use
This 2.5 axis plotter is intended to be used to plot images on a piece of paper. 
However, the main carriage of this plotter could be easily changed to accomodate 
a CO2 laser or small cutting blade to turn the plotter into a laser cutter or a 
vinyl cutter.  This project was just intended to be used by our team to demonstrate
many of the concepts that we learned in ME 405, Mechatronics, however I think it would 
be interesting to redesign some of the motor mounts to accept more consumer grade motors
so that we could each produce our own plotter for personal use. 
### BOM and Estimated Cost
| Qty. | Part                  | Source                | Est. Cost |
|:----:|:----------------------|:----------------------|:---------:|
|  2   | Pittperson Gearmotors | ME405 Tub             |     -     |
|  1   | Nucleo with Shoe      | ME405 Tub             |     -     |
|  1   | Motor H-Bridge        | ME405 Tub             |     -     |
|  1   | Purple Sharpie&trade; | Personal Supply       |     -     |
|  1   | Servo Motor           | Personal Supply       |     -     |
|  1   | Limit Switch pack     | Amazon                |   $6.99   |
|  1   | Vbearings and Belt    | Amazon                |   $18.59  |
|  1   | 2020 Al Extrusion     | Amazon                |   $19.99  |

### Sketch of Pen Plotter 
The initial sketch of our system is shown below. This design features prelinimary
dimensions and a sketch of the general shape and motion of our system. The blue lines
depict the direction that the system may move, and the axis that this motion occurs on.
For example, the curved blue arrows and the Theta axis show that our "arm" will rotate
about the larger base (Radius of 1"). The main features of this sketch are the base,
arm, carriage, and wheel. The exact shape and location of these parts, along with 
parts that are less significant to the general motion of our system are shown in the 
full system CAD model below. One thing that is not depicted in this sketch is how 
we actuated the 0.5 axis that will move the Sharpie up and down. This will be shown
in detail in the Main Carriage Subsystem CAD model section below. 

![Drawing of Proposed Plotter](https://github.com/dcejagon/Term-Project/blob/d55f55b985cb45acc1c4e1f98c530143e906ff7f/Project%20Sketch%20.png)
Initial Sketch of Plotter 


### Full System CAD Model
The image below shows our full system CAD model. The parts that are a light orange 
color are some the parts that we 3D printed. This image shows how the system will move;
the motor that is attached to the aluminum extrusion will rotate a pulley. This pulley 
will rotate a belt, who's ends are attached to the sharpie carriage in the slots. The
belt will be tensioned by being attached to a idle pulley on the aluminum extrusion
near the wheel.

The theta direction will also be actuated with belts and pulleys. The Theta motor
is fixed with set screws into the large, orange, triangle shaped, bracket. This motor 
has a pulley on it that is in plane with the larger red pulley in the image. These pulleys
have a belt that is attached around them, so when the motor rotates, the large 
pulley is rotated. This large red pulley is fixed to the aluminum extrusion with 
two bolts. This means that the red pulley cannot rotate relative to the extrusion,
which allows us to rotate the extrusion by rotating the Theta motor. This pulley is 
extended to hold three ball bearings that are press fit into the pulley. 
These bearings rotate on a 3/8" bolt which is the "axle" for our arm to rotate on.
In addition, the red pulley is around twice the diameter of the pulley attached to the motor 
which gives us a larger gear ratio to transmit more torque from the motor to our system. 

The large wheel on the end of the extrusion is necessasry to provide support to the 
end of our arm. The wheel prevents the arm from being a cantelevered beam, and reduces
the torque required to rotate the arm. 

Each of the motor mounting brackets have holes that have heat set inserts in them
so we can use screws to act as set screws to hold the motors in place. 

The motor bracket on the aluminum extrusion also holds a limit switch. This switch 
will act as a "kill switch" so that if the motor ever hits it, the motor duty will 
instantly be set to zero. This switch was initially going to be used to home the R
axis, however we had an issue where our motors would freespin after the program finished
running, and changing the switch to be a kill switch prevents the mechanical system 
from tearing itself apart and the motors from burning up. 

![CAD of Full System, Front](https://github.com/dcejagon/Term-Project/blob/f340f8d59cd680c3848f8afeec37d6229f56b2f1/FullSysCAD.png)
CAD model of full system front view

![CAD of Full System, Rear](https://github.com/dcejagon/Term-Project/blob/f340f8d59cd680c3848f8afeec37d6229f56b2f1/FullSysCAD2.png)
CAD model of full system rear view


### Main Carriage Subsystem CAD Model

The image below shows the main sharpie carriage in more detail. The black piece
is the "carriage" that has bolts that go through it and have V-Slot bearings on
the back side (shown as the gray cylinders at the top of the image). These bearings
ride in the T-slot on the aluminum extrusion, allowing for smooth, linear movement
of the carriage on the extrusion. 

The blue rectangular piece is the servo motor that is responsible for actuating our 
half axis. The servo motor is attached to the carriage with rubber bands so it can
be repurposed for other projects. The servo motor has a small link (white part) attached to it.
This link has a hole on one side to press fit onto the servo shaft, and a slot 
on the other. This slot will have a "pin" that attaches to the sliding carriage 
where the Sharpie is attached. When the servo motor is rotated, the slotted linkage
rotates , which pushes against pin attached to the Sharpie carriage, causing 
vertical movement of the Sharpie carriage. 

The small, "r" shaped slots on either side of the main carriage are where the ends
of the belt to move the main carriage are attached.  

![CAD of main carriage, raised](https://github.com/dcejagon/Term-Project/blob/f340f8d59cd680c3848f8afeec37d6229f56b2f1/SharpieCarriageUp.png)
CAD model of main carriage in "up" position


![CAD of main carriage, lowered](https://github.com/dcejagon/Term-Project/blob/f340f8d59cd680c3848f8afeec37d6229f56b2f1/SharpieCarriageDown.png)
CAD model of main carriage in "down" position

### Software Design Overview
In order to generate the path that the pen should take, we used http://jscut.org/jscut.html# ,
a website that accepts SVG images and converts it to GCODE. This website was nice, because 
each of the GCODE lines were G1, which is the call for a straight line. The GCODE that 
this website outputs is a series of straight lines that are very short (around 0.001"). 
This means, we essentially have a list of X-Y coordinates that trace out our image. 

We then use the file GcodeInterpreter.py, to take each line of GCODE, pull out the 
desired X-Y coordinates, and then preform some math to convert these to R-Theta
coordinates. From these R-Theta coordinates, we use our known gear ratios to write
the desired R Motor angle and Theta Motor angle to their own .txt files. 

We then read each line of these files one at a time, to generate the desired
R and Theta motor setpoints. 

We then input these setpoints into a closed loop controller which will calculate the
required duty to move the motor so that the motor position reaches the setpoint. 

We determine the motor position from encoders that are attached to the motor shaft. 

The timing of these different tasks was soemthing that we had some trouble implementing,
however, we were able to achieve the propper timing by adding two buffer variables. 
Essentially, first, we get both setpoints, then, the motors rotate to try and reach that setpoint
next, we check to see if each motor has reached its setpoint (or within a few degrees of it).
If the motor has not reached this setpoint, we do not get another setpoint. As soon as the motor 
reaches its setpoint, on its next loop around the task diagram, we generate a new setpoint. 
This process allows us to be sure that our motors reach their desired setpoint before they
transition to another one. 

In addition, the motor control task has three sub-tasks running. 
First, we read the motor positon from the encoders. Next, we run the closed loop
controller. Last, we use the motor duty that comes out of the closed loop file
to run our motors at this duty. It is important that the motor control task runs 
as quickly as possibleso that the closed loop controller can calculate be sure the
motor reaches the desired positon as quickly as possible, while minimising overshoot. 

Lastly, we had a task that controlled the limit switch reading and servo motor actuation.
The limit switch subtask checks the limit switch value (0 or 1) and decides if the duty needs to be set 
to zero. The servo motor subtask checks to see if the pen should lifted or lowered,
and then raised or lowers the servo motor. 

A more in-depth description of each file, along with the overall software structure
can be found in the links below. 

GCODE Interpreter:         [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/GcodeInterpreter.py] \n
Encoder Driver:            [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/EncoderDriver.py]
Closed Loop Controller:    [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/RMotorControl.py]
Motor Driver:              [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/MotorDriver.py]
Limit Switch:              [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/LimitSwitch.py]
Servo Motor:               [https://github.com/dcejagon/Term-Project/blob/e9a6a358911b557f958eb8ccfb334c0a805cc6d8/src/ServoMotorF.py]


### System Preformance and Results
We tested our system by trying to draw several images. We attempted to draw a 
Cal Poly logo, as well as a simple rectangle. These test revealed some errors
in our software design somewhere. We were able to successfully draw, however, we
were not able to produce a discernable image. We believe that it has somehting to 
do with the path the pen is taking between the points. For the rectangle, we can see
the image has four distict "points", but the paths between these points is anything 
but a straight line. With more time, we would be able to hammer out the bugs in
our system and correct the paths between points. Overall, we are happy with what 
we were able to accomplish during the entirety of this project. 

### Possible System Modifications
Outside of the path issue mentioned above, one of our biggest issues was the 
resolution our motors were able to acomplish. We think that we prioritized speed 
more than accuracy, which means we tried to minimize the gear ratios that we were 
using. The motors we were using have a minimum duty that will make them rotate. 
Significant issues arrise when the desired position is too close to the previous 
position, becasue the motor cannot rotate with this small of a duty. By increasing 
the gear ratios we are using significantly, we would increase the resolution that 
we can plot. Instead of 2 points that are very close producing a duty of 10 for example,
with the increased gear ratio, we can have the same two points, produce a duty of 50 or even 100.
This would allow for our plotted pictures to be very clear, with the effect of 
significantly decreasing the speed at which we can plot. 

In addition, we should have had our platform 
that the parts are mounted to extend out so that every part of the system rests
on this platform. This would mininimize the amount of flex from the point of rotation
to the end of the extrusion. 

One of the last things that was somewhat of an issue, was our heat set inserts. 
When we tightened the screws to hold the motor in place, the inserts began to pull 
out of their holes. We think this could be resolved by reducing the size of the holes
or using different inserts. 

Some of the things that do not need modification is how the main carriage rides on
the aluminum extrusion. We are able to produce a very smooth linear movement of the
carriage when we rotate the motor. In addition, the way the way our differnet tasks
iteracted with eachother was largely successful. Once we figured out the propper 
timing, our software worked as intended, and ironing out the path issue would
not require much rework to our task layout. 

Here is the link to the folder that contains all of our solidworks files as well
as STL's used for 3D printing. 
[https://github.com/dcejagon/Term-Project/tree/bce21b94aa009a9af5754362cd7ddc3f18eb79eb/TP%20CAD]