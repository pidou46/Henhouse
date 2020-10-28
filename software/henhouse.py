
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
#import network
# wlan = network.WLAN(network.STA_IF) # create station interface
# wlan.active(True)       # activate the interface
# wlan.connect('essid', 'password') # connect to an AP
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses


#update RCT time form network
#import ntptime
#ntptime.settime()

#calculate sunrise/sunset time
#import sun
#coords = {'longitude' : 2.107, 'latitude' : 44.584 }
#sun = Sun()
# Sunrise time UTC (decimal, 24 hour format)
#print(sun.getSunriseTime( coords )['decimal'])
# Sunset time UTC (decimal, 24 hour format)
#print(sun.getSunsetTime( coords )['decimal'])

#scheduling
#
#from machine import Timer, RTC
#tim=Timer()
#rtc=machine.RTC()
#if sunrise<nowDecimal()<sunset :
#    tim.init(mode=Timer.ONE_SHOT,period=(sunset-nowDecimal)*1000,closeDoor()) # door action
#    # schedule next wakeup alarm 1min too early to accommodate RCT drift
#    rtc.alarm(rtc.ALARM0, sunrise-nowDecimal-60000) # alarm (ms)
#else
#    tim.init(mode=Timer.ONE_SHOT,period=(sunrise-nowDecimal)*1000,openDoor())
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
#stopTim.init(mode=Timer.ONE_SHOT,period=stroke,move())

#stop door() "callback"
#pwm2.deinit()


