# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:18:34 2022

@author: kepte
"""
#from matplotlib import pyplot as plt
import math
    
class GcodeInterpreter:
    
    def __init__(self,ThetaArray,RArray,setpoint1,setpoint2):
        '''! initializes. x and y represent the columns that are used for 
             the respective data. enter either in the console or script below
             corresponding column for x and y to be used for the plot. 
        '''
        self.ThetaArray = ThetaArray
        self.RArray = RArray
        self.setpoint1 = setpoint1
        self.setpoint2 = setpoint2
        self.Theta = [] 
        self.R = []

        
    def read (self,fileName):
        '''! opens the text file and reads all data contained
             goes line by line, searching for lines with relevant x and y coord data. extracts data and stores it in list.
        '''
        
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
        '''
        self.x = []
        self.Theta = []
        for line in self.mylines:
            if 'X' in line:
                val = float(line[4:10])
                self.x.append(val)
            else:
                pass
        return self.x
       
        
    def YExtract (self):
        '''! Extracts the Y values from list of data and floats elements.
        '''
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
        '''
        self.z = []
        for line in self.mylines:
            if 'Z0' in line:
                self.z.append(0)
            elif 'Z-' in line:
                self.z.append(1)
        return self.z
    
    def ThetaConvert (self):
        '''! Intakes extracted x and y values and converts them into corresponding angles for the encoder to read for theta position
        '''
        for i in range(0, len(self.x)):
            self.Theta.append(math.atan((self.y[i]/self.x[i])*180/math.pi)*16384/360)
            
        
            
        return self.Theta
    def RConvert (self):
        '''! Intakes extracted x and y values and converts them into corresponding angles for the encoder to read for R position
        '''
        for i in range(0, len(self.x)):
            R_len=math.sqrt(self.x[i]**2+self.y[i]**2)
            lintotick=360/1.51
            self.R.append(R_len*lintotick)
            
        return self.R
        
    
        
    def ShareGen (self):
        '''! Takes converted data and passes it into position shares one line at a time to be used by motor controllers.
        '''
        for line in self.RArray:
            self.setpoint1.put(self.ThetaArray)
            self.setpoint2.put(self.RArray)
            
        yield self.setpoint1, self.setpoint2
        
            
        
    
    # def plot (self):
    #       ''' generates the desired plot to verify gcode.
    #       '''
         
    #       plt.plot(self.x,self.y, color='purple', linestyle='dashed')
    #       #plt.grid(color='orange', linestyle='-', linewidth=1)
    #       plt.xlabel('x position')
    #       plt.ylabel('y position')
    #       plt.title('Verification Display')
    #       plt.show()
          
    def AIO (self,fileName):
        
        self.mylines = []
        with open(fileName) as f:
            for line in f:
                if 'G1' in line:
                    self.mylines.append(line)
                else:
                    pass
                
        self.x = []
        self.Theta = []
        for line in self.mylines:
            if 'X' in line:
                val = float(line[4:10])
                self.x.append(val)
            else:
                pass
            
        self.y = []
        for line in self.mylines:
            if 'Y' in line:
                val = float(line[12:19])
                self.y.append(val)
            else:
                pass
            
        self.z = []
        for line in self.mylines:
            if 'Z0' in line:
                self.z.append(0)
            elif 'Z-' in line:
                self.z.append(1)
                
        for i in range(0, len(self.x)):
            self.Theta.append(math.atan((self.y[i]/self.x[i])*180/math.pi)*16384/360)
            
        for i in range(0, len(self.x)):
            R_len=math.sqrt(self.x[i]**2+self.y[i]**2)
            lintotick=360/1.51
            self.R.append(R_len*lintotick)
            
        self.ThetaArray.put(self.Theta)
        self.RArray.put(self.R)
            
        return self.ThetaArray , self.RArray
        
        

if __name__ == '__main__':
    d = GcodeInterpreter()
    #full_code = d.read('gcode.txt')
    # x_val = d.XExtract()
    # y_val = d.YExtract()
    # z_val = d.ZConvert()
    # theta_val = d.ThetaConvert()
    # r_val = d.RConvert()
    aio = d.AIO('gcode.txt')
    share_val = d.ShareGen()
    d.plot()