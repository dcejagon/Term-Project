'''
@file                mainpage.py
@brief               Brief doc for mainpage.py
@details             Detailed doc for mainpage.py 

@mainpage

@section sec_intro   ME 405 Term Project
                        This is our project main page for the ME 405 plotter project
                        
                        Our Source Code Repository can be found:  \htmlonly <a href="https://github.com/dcejagon/Term-Project/tree/main/Temporary">here</a> \endhtmlonly

@section sec_lb1     Task Diagram and File Structure 
   
We developed the Task Diagram seen below to demonstrate the file structure that we plan to use in our 2D plotter. 
Each of the files will have some combination of shares and/or queues in order to allow for variable 
data to be shared between files. We will utilize this by using the Task_Shares.py file
that we have been provided to ensure the variables are set up correctly. 
In addition, we plan to have the differnet tasks communicate with eachother using 
the structure outlined in previous labs and by using CoTasks.py to make sure we 
are taking advantage of cooperative multitasking.  
            
\htmlonly
<iframe width="560" height="315" src="https://www.youtube.com/embed/-y_-CNrFDrs" title="Task Diagram" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
\endhtmlonly
            
@section sec_lb2    FSM for each task
    
    
Below we have imagees of the finite state machine (FSM) we plan to use for some of our tasks.
Many of these have just two states, "On" and "Off" but the transitions unique to each task
is shown below. 


\htmlonly
<iframe width="560" height="315" src="https://www.youtube.com/embed/wGd1_bI-Tz8" title="FSM for ______" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
\endhtmlonly



@author              Nolan Clapp
@author              Caleb Kephart
@author              Daniel Gonzalez

@copyright           Open Source

@date                Feb 22, 2022
'''