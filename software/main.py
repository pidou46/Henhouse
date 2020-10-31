import network, time

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('TNCAP31A0C1', '16EC3AD4F1') # connect to an AP
wlan.config('mac')      # get the interface's MAC address

print(wlan.ifconfig())    # get the interface's IP/netmask/gw/DNS addresses

while True:
    print(str(wlan.status('rssi'))+"dBm 70 OK")
    time.sleep(5)