# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:56:00 2022

@author: nclap
"""
class LimitSwitch:
    
    def __init__(self,switchpin1,switchpin2):
        self.switch_pin1=switchpin1
        self.switch_pin2=switchpin2
   
    def checkswitch(self):
        R=self.switch_pin1.value()
        T=self.switch_pin2.value()
        
        if R==1:
            pass
        elif R==0:
            self.duty2.put(0)
        
        if T==1:
            pass
        elif T==0:
            self.duty1.put(0)
        