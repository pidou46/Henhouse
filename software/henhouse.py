import network, ntptime
from time import localtime
from sun import Sun
from machine import Timer, RTC, Pin, PWM
import machine

#device is waking up by an alarm scheduled by itself earlier or by first start
#Connect to network
#synchronise is internal clock to accommodate internal RTC drift and set the "now" variable
#calculate sunrise / sunset at location and actual date
#scheduling the next door movement deide if it shoud open or close depending on now and sunrise /sunset values

H_TO_MS=3600000 # decimal hour to ms : 60*60*1000=3600000_ms=1_h

STROKE=4500 # stroke 45000_ms / 300_mm => 150_ms/mm@1200_Hz
DIR_PIN=22
STEP_PIN=21



#Check if device woke from deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    p1=Pin(4, Pin.OUT, None) # un-hold internal pullup

#connect to network
SSID='TNCAP31A0C1'
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
try:
    wlan.connect('TNCAP31A0C1', '16EC3AD4F1') # connect to an AP
    print("device connected to SSID {}: {}".format(SSID,wlan.isconnected()))
    print("IP adress {}".format(wlan.ifconfig()[0]))         # get the interface's IP/netmask/gw/DNS addresses
    print("RSSI {}".format(wlan.status('rssi')))
except:
    pass
    
#update RCT time form network
ntptime.host = 'pool.ntp.org'
#ntptime.settime()
now=float("{}.{}".format(localtime()[3],localtime()[4]))
print("time: {}".format(localtime()))

#calculate sunrise/sunset time
coords = {'longitude' : 2.107, 'latitude' : 44.584 }
sun = Sun()
# Sunrise time UTC (decimal, 24 hour format)
sunrise=sun.getSunriseTime( coords )['decimal']
print("Sunrise (UTC decimal) : {}".format(sunrise))
# Sunset time UTC (decimal, 24 hour format)
sunset=sun.getSunsetTime( coords )['decimal']
print("Sunset (UTC decimal): {}".format(sunset))

#scheduling


stepPin = PWM(Pin(STEP_PIN), freq=0, duty=32)
stopTim=Timer(1)
dirPin=Pin(DIR_PIN, Pin.OUT)

#override now variable for testing
now=7.45

#callback
def closeDoor(_):
    dirPin.value(0)
    print("Close the door")
    stepPin.freq(1000) # start movement
    stopTim.init(mode=Timer.ONE_SHOT,period=STROKE,callback=stopDoor)
    return

#callback
def openDoor(_):
    dirPin.value(1)
    print("Open the door")
    stepPin.freq(1000) #start movement
    stopTim.init(mode=Timer.ONE_SHOT,period=STROKE,callback=stopDoor)
    return

#callback
def stopDoor(_):
    print("Stop mouvement")
    stepPin.deinit() #stop movement
    #disable drv8825 to save energy
    return

tim=Timer(0)
rtc=RTC()
if sunrise < now < sunset :
    print("Woken during dailight, scheduling evening actions.")
    period=int(round((sunset-now)*H_TO_MS))
    print("snooze period: {}_h - {}_ms".format(period/H_TO_MS, period))
    tim.init(mode=Timer.ONE_SHOT,period=period,callback=closeDoor) # door action
    # compute duration to next wakeup 
    period=((24-now+sunrise)*H_TO_MS)
else:
    print("Woken at night, scheduling morning actions.")
    period=int(round((sunrise-now)*H_TO_MS))
    print("snooze period: {}_h - {}_ms".format(period/H_TO_MS, period))
    tim.init(mode=Timer.ONE_SHOT,period=period,callback=openDoor)
    # compute duration to next wakeup 
    period=((sunset-now)*H_TO_MS)

#alarm 1min too early to accommodate RCT drift
period=period-60000 # 60000=1_min
print("next wakeup: {}_h - {}_ms".format(period/H_TO_MS, period))


#put device in deepsleep
#p1=Pin(4, Pin.IN, Pin.PULL_HOLD) # save power
#machine.deepsleep(period) # (ms)

#if __name__=="__main__":
    