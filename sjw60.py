#!/usr/bin/python
# gpiotester.py
# Blinks USR1 and USR2, plus external LED connected to Port 8 Pin 3 of the Beaglebone
# -- must be run as root
import time
from time import gmtime, strftime

readIt = 1
gpioHiCnt = 0
gpioLoCnt = 0
gpioLoLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
gpioHiLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
lastLoTime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
lastHiTime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
lastVal = 35
# put Port 8 Pin 3 into mode 7 (GPIO)
#open('/sys/kernel/debug/omap_mux/gpmc_ad6', 'wb').write("%X" % 7)
    
try: 
    # check to see if the pin is already exported
    open('/sys/class/gpio/gpio60/direction').read()
except:    
    # it isn't, so export it
    print("exporting GPIO 60")
    open('/sys/class/gpio/export', 'w').write('60')

    
# set Port 8 Pin 3 for output    
if readIt:
    open('/sys/class/gpio/gpio60/direction', 'w').write('in')
else:
    open('/sys/class/gpio/gpio60/direction', 'w').write('out')
    open('/sys/class/gpio/gpio60/value', 'w').write('1')

if readIt:
    while 1:
        red = open('/sys/class/gpio/gpio60/value').read()
        comp = red.rstrip()
        mstr = "__"
        #mstr += str(type(red))
        mstr += comp
        mstr += "__"
        print mstr
        if(comp== '1'):
            print "gottit"
            gpioHiCnt += 1
            gpioHiLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        #if(red==0):
        else:
            gpioLoCnt += 1
            gpioLoLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        if(lastVal == comp) :
            #do nothing
            dummy = 1    
        else :
            lastVal = comp
            if(lastVal == '1') :
                lastLoTime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            else :
                lastHiTime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        mstr = "Lo::P9_12, %d, " % gpioLoCnt
        #mstr += gpioLoLast
        mstr += lastLoTime
        print mstr.strip()
        mstr = "Hi::P9_12, %d, " % gpioHiCnt
        #mstr += gpioHiLast
        mstr += lastHiTime
        print mstr.strip()

        #print red
        mstr = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        mstr += red.rstrip()
        mstr += (" %d" % gpioHiCnt)
        mstr += (" %d" % gpioLoCnt)
        print mstr
        time.sleep(1)
        
    
    
    
# we will assume that USR1 and USR 2 are already configured as LEDs    
    
#for i in range(10):
#    # turn on USR1 and external LED
#    open('/sys/class/gpio/gpio60/value', 'w').write("1")
#    open("/sys/devices/platform/leds-gpio/leds/beaglebone::usr1/brightness", 'w').write("1")
#    # turn off USR2
#    open("/sys/devices/platform/leds-gpio/leds/beaglebone::usr2/brightness", 'w').write("0")
#
#    time.sleep(1)
#    
#    # turn off USR1 and external LED
#    open('/sys/class/gpio/gpio60/value', 'w').write("0")
#    open("/sys/devices/platform/leds-gpio/leds/beaglebone::usr1/brightness", 'w').write("0")
#    # turn on USR2
#    open("/sys/devices/platform/leds-gpio/leds/beaglebone::usr2/brightness", 'w').write("1")    
#
#    time.sleep(1)
        
# cleanup - remove GPIO60 folder from file system
#open('/sys/class/gpio/unexport', 'w').write('60')
      
        
    
