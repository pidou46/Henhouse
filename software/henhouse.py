import network, ntptime
from time import localtime
from sun import Sun
from machine import Timer, RTC, PWM



#device is waking up by an alarm scheduled by itself earlier or by first start
#Connect to network
#synchronise is internal clock to accommodate internal RTC drift and set the "now" variable
#calculate sunrise / sunset at location and actual date
#scheduling the next door movement deide if it shoud open or close depending on now and sunrise /sunset values


#Check if device woke from deep sleep
#if machine.reset_cause() == machine.DEEPSLEEP_RESET:
#   print('woke from a deep sleep')
#p1=Pin(4, Pin.OUT, None) # un-hold internal pullup

#connect to network
SSID='TNCAP31A0C1'
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('TNCAP31A0C1', '16EC3AD4F1') # connect to an AP
print("device connected to SSID {} with IP adress {}".format(SSID,wlan.ifconfig()[0]))         # get the interface's IP/netmask/gw/DNS addresses
print("RSSI {}".format(wlan.status('rssi')))

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
#
tim=Timer(0)
rtc=RTC()
if sunrise < now < sunset :
    print("wake in the morning")
    #tim.init(mode=Timer.ONE_SHOT,period=(sunset-now)*1000,callback=closeDoor) # door action
#    # schedule next wakeup alarm 1min too early to accommodate RCT drift
#    rtc.alarm(rtc.ALARM0, sunrise-nowDecimal-60000) # alarm (ms)
else:
    print("wake in the evening")
    #tim.init(mode=Timer.ONE_SHOT,period=(sunrise-now)*1000,callback=openDoor)
#    # schedule next wakeup alarm 1min too early to accommodate RCT drift
#    rtc.alarm(rtc.ALARM0, sunset-nowDecimal-60000) # alarm (ms)


#wait for door action to be done
#sensor or timer ?
#disable drv8825 to save energy

#put device in deepsleep
#p1=Pin(4, Pin.IN, Pin.PULL_HOLD) # save power
#machine.deepsleep()

#move door(state) "callback"
#from machine import PWM
#p_en=Pin(5, Pin.OUT)
#p_dir=Pin(4, Pin.OUT)
##enable drv8825
#p_en.on()
##set dir
#p_dir.value(state) #state=1 : ouvert
#pwm2 = PWM(Pin(2), freq=1000, duty=512)
#stopTim.init(mode=Timer.ONE_SHOT,period=stroke,move()) # stroke 45000_ms / 300_mm => 150_ms/mm@1200_Hz

#stop door() "callback"
#pwm2.deinit()

def closeDoor():
    return

def openDoor():
    return
