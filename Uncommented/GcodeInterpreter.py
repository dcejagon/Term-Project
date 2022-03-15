''' @file                       GcodeInterpreter.py
    @brief                      File which interprets gcode and converts values into usable data for motor encoders.
    @details                    Opens a gcode file and extracts position data and converts to polar coordinates. Plots data for verification and writes data to two text files to be used by the onboard program.
                                
    @author                     Daniel Gonzalez
    @author                     Nolan Clapp
    @author                     Caleb Kephart
    @date                       March 14, 2022
'''
from matplotlib import pyplot as plt
import math
import time  
class GcodeInterpreter:
    
    #def __init__(self,ThetaArray,RArray,setpoint1,setpoint2):
    def __init__(self):
        '''! initializes class and arrays for data collection for generated text documents
        '''
        # self.ThetaArray = ThetaArray
        # self.RArray = RArray
        # self.setpoint1 = setpoint1
        # self.setpoint2 = setpoint2
        
        ## @brief  Array set up to collect data points for the arm angle position.
        #
        self.Theta = [] 
        ## @brief  Array set up to collect data points for the position along the arm.
        #
        self.R = []
        ## @brief Array set up to collect arm angle data converted to polar coordinates.
        #
        self.Thetaradi = []
      
        
    def read (self,fileName):
        '''! opens the text file and reads all data contained
             goes line by line, searching for lines with relevant x and y coord data. extracts data and stores it in list.
             
             @param fileName: file name of input gcode
             @return mylines: array of relevant lines of gcode.
        '''
        ## @brief Extracts relevant lines from gcode to acquire x and y coordinates
        #
        self.mylines = []
        with open(fileName) as f:
            for line in f:
                if 'G1' in line:
                    self.mylines.append(line)
                else:
                    pass
                    
            
            return self.mylines
  
    def XExtract (self):
        '''! Extracts the X values from list of data and floats elements.
            @return x: Extracted x coordinates from gcode
        '''
        ## @brief Extracted x coordinates from gcode
        #
        self.x = []
        self.Theta = []
        for line in self.mylines:
            if 'X' in line:
                ## @brief floats strings within mylines
                #
                val = float(line[4:10])
                
                self.x.append(val)
            else:
                pass
        return self.x
       
        
    def YExtract (self):
        '''! Extracts the Y values from list of data and floats elements.
            @return y: Extracted y coordinates from gcode
        '''
        ## @brief Extracted y coordinates from gcode
        #
        self.y = []
        for line in self.mylines:
            if 'Y' in line:
                val = float(line[12:19])
                self.y.append(val)
            else:
                pass
        return self.y
    
    def ZConvert (self):
        '''! Extracts Z values and converts into values for servo to read to engage/disengage.
            @return z: Extracted z plunging positions from gcode.
        '''
        ## @brief Extracted z coordinates from gcode
        #
        self.z = []
        for line in self.mylines:
            if 'Z0' in line:
                self.z.append(0)
            elif 'Z-' in line:
                self.z.append(1)
        return self.z
   
    
    def ThetaConvert (self):
        '''! Intakes extracted x and y values and converts them into corresponding angles for the encoder to read for theta position
            @return Theta:  Array set up to collect data points for the arm angle position.
            @return  Thetaradi:  Array set up to collect arm angle data converted to polar coordinates.
        '''
        for i in range(0, len(self.x)):
            self.Theta.append((math.atan(self.y[i]/self.x[i])*180/math.pi))
            self.Thetaradi.append((math.atan(self.y[i]/self.x[i])))

            
        
            
        return self.Theta, self.Thetaradi
    def RConvert (self):
        '''! Intakes extracted x and y values and converts them into corresponding angles for the encoder to read for R position
            @return  R: Array set up to collect data points for the position along the arm.
        '''
        for i in range(0, len(self.x)):
            R_len=math.sqrt(self.x[i]**2+self.y[i]**2)
            lintodeg=360/1.51
            self.R.append(R_len*lintodeg)
            
        return self.R
        
    
        
    # def ShareGen (self):
    #     '''! Takes converted data and passes it into position shares one line at a time to be used by motor controllers.
    #     '''
    #     for line in self.RArray:
    #         self.setpoint1.put(self.ThetaArray)
    #         self.setpoint2.put(self.RArray)
            
    #     yield self.setpoint1, self.setpoint2
        
            
        
    
    def plot (self):
          ''' generates the desired plot to verify gcode.
          '''
         
          plt.plot(self.x,self.y, color='purple', linestyle='dashed')
          #plt.grid(color='orange', linestyle='-', linewidth=1)
          plt.xlabel('x position')
          plt.ylabel('y position')
          plt.title('Verification Display')
          plt.show()
          
    def plotpol (self):
        '''! Generates plot of interpreted gcode using polar coordinates.
        '''
        plt.polar(self.Thetaradi,self.R)
        plt.show
          
    # def AIO (self,fileName):
        
    #     self.mylines = []
    #     with open(fileName) as f:
    #         for line in f:
    #             if 'G1' in line:
    #                 self.mylines.append(line)
    #             else:
    #                 pass
                
    #     self.x = []
    #     self.Theta = []
        
    #     for line in self.mylines:
    #         if 'X' in line:
    #             val = (float(line[4:10])+100)
    #             self.x.append(val)
                
    #         else:
    #             pass
            
    #     self.y = []
    #     for line in self.mylines:
    #         if 'Y' in line:
    #             val = float(line[12:19])
    #             self.y.append(val)
    #         else:
    #             pass
            
    #     self.z = []
    #     for line in self.mylines:
    #         if 'Z0' in line:
    #             self.z.append(0)
    #         elif 'Z-' in line:
    #             self.z.append(1)
                
    #     for i in range(0, len(self.x)):
    #         self.Theta.append((math.atan(self.x[i]/self.y[i]))*(180/math.pi))#*16384/360)
            
    #     for i in range(0, len(self.x)):
    #         R_len=math.sqrt(self.x[i]**2+self.y[i]**2)
    #         lintotick=360/1.51
    #         self.R.append(R_len*lintotick)
            
    #     # self.ThetaArray.put(self.Theta)
    #     # self.RArray.put(self.R)
            
    #     # return self.ThetaArray , self.RArray
    #     return(self.R,self.Theta)
        
    def TxtCreate (self):
        '''! Creates two text files on board the pybflash to be used to pull positional data from to control the motors. 
             One file for R values (along the arm), and another for theta values (angle of the arm).
        '''
        with open("Rcode.txt", "w") as f:
            ## @brief Takes floats from the R array and converts to strings so that they can be written to txt file.
            #
            R_str = str(self.R)
            f.write(R_str)
        
        with open("Tcode.txt", "w+") as g:
             ## @brief Takes floats from the Theta array and converts to strings so that they can be written to txt file.
            #
            Theta_str = str(self.Theta)
            g.write(Theta_str)
        
if __name__ == '__main__':
    d = GcodeInterpreter()
    full_code = d.read('simple.txt')
    x_val = d.XExtract()
    y_val = d.YExtract()
    z_val = d.ZConvert()
    theta_val = d.ThetaConvert()
    r_val = d.RConvert()
    #theta_rad =d.ThetaRad()
    # aio = d.AIO('SQUARE.txt')
    # share_val = d.ShareGen()
    d.plot()
    d.plotpol()
    d.TxtCreate()