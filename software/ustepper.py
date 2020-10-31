# drv8825 driver
from machine import Pin, PWM, Timer
import time

class Stepper:
    def __init__(self, dirPin, stepPin, m0, m1):
        self.dirPin=dirPin
        self.stepPin=PWM(stepPin, freq=0, duty=0)
        self.m0=m0 #microstep pin M0
        self.m1=m1
        #M0,M1,M2,ms
        self.timeTable=[(1,1,0,512),(0,1,0,512),(1,0,0,512),(0,0,0,45000),(1,0,0,512),(0,1,0,512),(1,1,0,512)]
        self.tim=Timer(-1)
        self.stepPin.freq(1200)
        self.index=0

    #travel (in steps), speed (in steps / seconds)
    def Schedule(self, travel, speed):
        #converti les steps en millisecondes en tenant compte
        #cree une rampe d'acceleration / deceleration par paliers
        #en utilisant les microsteps
        
        #for i in  
        #    self.timeTable[]int(steps/self.freq)*1000)
        pass

    #integre une compensation du temps du retard moyen du Timer (1_ms)
    def Run(self, t):
        self.stepPin.duty(32)
        self.dirPin.value(1)
        try:
            print(time.ticks_us())
            #le changement d'etat des pins de microstep sequenciel
            #peut poser des problemes il vaudrait mieux un changement
            #d'etat synchronise: solution avec GPIO_OUT_REG a implementer
            #solution alternative avec code viper a priorie plus rapide?
            #voir post forum: 
            self.m0.value(self.timeTable[self.index][0])
            self.m1.value(self.timeTable[self.index][1])
            self.tim.init(period=(self.timeTable[self.index][3])-1, mode=Timer.ONE_SHOT, callback=self.Run)
            self.index+=1
        except:
            self.stepPin.duty(0)

if __name__ == '__main__':
    #dirPin, stepPin, m0
    test=Stepper(Pin(22, Pin.OUT),Pin(21),Pin(15, Pin.OUT),Pin(13,Pin.OUT))
    test.Run(0)
    while True:
        print('meanwhile...')
        time.sleep(1)

#290696176  
#292696529  2000353
#312696887  20000358
#314697197  2000310
#avec une compensation de 1_ms la deviation est d'environ:
#300_us a chaque changement de palier
        
