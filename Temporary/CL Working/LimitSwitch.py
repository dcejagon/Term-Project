# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:56:00 2022

@author: nclap
"""
class LimitSwitch:
    
    def __init__(self,switchpin1,switchpin2,duty2):
        self.switchpin1=switchpin1
        self.switchpin2=switchpin2
        self.duty2=duty2
    print('initializing limit switch')
    def checkswitch(self):
        
        #R=self.switch_pin1.value()
        #T=self.switch_pin2.value()
        
        if self.switchpin1.value()==1:
            print('val=1')
            self.Rswitch.put(self.switchpin1.value())
            print(self.Rswitch.get())
            
        
        elif self.switchpin1.value()==0:
            print('val=2')
            self.Rswitch.put(self.switchpin1.value())
            self.duty2.put(0)
            print(self.Rswitch.get())
        
        # if T==1:
        #     pass
        # elif T==0:
        #     self.duty1.put(0)
        