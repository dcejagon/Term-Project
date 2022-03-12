# Term Project Proposal 
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
### Preliminary BOM and Estimated Cost
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

### Sketch of Proposed Plotter 
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

![CAD of Full System](https://github.com/dcejagon/Term-Project/blob/1b538ee28f59977871e3b20c34f9b20de40c2d71/maincar.png)
CAD model of full system

### Main Carriage Subsystem CAD Model

The image below shows the main sharpie carriage in more detail. The black piece
is the "carriage" that has bolts that go through it and have V-Slot bearings on
the back side (shown as the gray cylinders at the top of the image). These bearings
ride in the T-slot on the aluminum extrusion, allowing for smooth, linear movement
of the carriage on the extrusion. 

The blue rectangular piece is the servo motor that is responsible for actuating our 
half axis. The servo motor is attached to the carriage with rubber bands so it can
be repurposed for other projects. The servo motor has a small link attached to it.
This link has a hole on one side to press fit onto the servo shaft, and a slot 
on the other. This slot will have a "pin" that attaches to the sliding carriage 
where the Sharpie is attached. When the servo motor is rotated, the slotted linkage
rotates , which pushes against pin attached to the Sharpie carriage, causing 
vertical movement of the Sharpie carriage. 

The small, "r" shaped slots on either side of the main carriage are where the ends
of hte belt to move the main carriage are attached.  

![CAD of main carriage](https://github.com/dcejagon/Term-Project/blob/1b538ee28f59977871e3b20c34f9b20de40c2d71/maincar.png)
CAD model of main carriage 