# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:18:34 2022

@author: kepte
"""
from matplotlib import pyplot as plt
    
class GcodeInterpreter:
    
    def __init__(self):
        ''' initializes. x and y represent the columns that are used for 
            the respective data. enter either in the console or script below
            corresponding column for x and y to be used for the plot. 
        '''
        
      
        

        
    def read (self,fileName):
        ''' opens the csv file and reads all data contained
        '''
        self.mylines = []
        with open(fileName) as f:
            for line in f:
                if 'G1' in line:
                    self.mylines.append(line)
                else:
                    pass
                    
            
            return self.mylines
  
    def XConvert (self):
        self.x = []
        for line in self.mylines:
            if 'X' in line:
                val = float(line[4:10])
                self.x.append(val)
            else:
                pass
        return self.x
        
        
    def YConvert (self):
        self.y = []
        for line in self.mylines:
            if 'Y' in line:
                val = float(line[12:19])
                self.y.append(val)
            else:
                pass
        return self.y
    
    def ZConvert (self):
        self.z = []
        for line in self.mylines:
            if 'Z0' in line:
                self.z.append(0)
            elif 'Z-' in line:
                self.z.append(1)
        return self.z
    
    def plot (self):
          ''' generates the desired plot tracking random student.
          '''
         
          plt.plot(self.x,self.y, color='purple', linestyle='dashed')
          #plt.grid(color='orange', linestyle='-', linewidth=1)
          plt.xlabel('x position')
          plt.ylabel('y position')
          plt.title('Verification Display')
          plt.show()

if __name__ == '__main__':
    d = GcodeInterpreter()
    full_code = d.read('gcode.txt')
    x_val = d.XConvert()
    y_val = d.YConvert()
    z_val = d.ZConvert()
    d.plot()