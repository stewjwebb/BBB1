#!/usr/bin/python


import time
from time import gmtime, strftime
#gpio_names[gpioId] = "name" 
#eg:
#gpio_names[60] = "P9_12"
#gpio_trigger[gpioId] = 0/1
#gpio_LoCnt[gpioId] = 0
#gpio_HiCnt[gpioId] = 0


gpio_names = ["nil" for i in range(256)] #i think there are 141 gpios
gpio_trigger = [0 for i in range(256)]
gpio_LoCnt = [0 for i in range(256)]
gpio_HiCnt = [0 for i in range(256)]
gpio_LastHiTime = ["nil" for i in range(256)]
gpio_LastLoTime = ["nil" for i in range(256)]
gpio_lastVal = [-1 for i in range(256)]

gpio_names[60] = "P9_12"
gpio_names[115] = "P9_27"

def openGpioForRead(id):
    gpioStr = "/sys/class/gpio/gpio%d" % id
    gpioDir = gpioStr + "/direction"

    tstr = "%s" %gpioDir

    try:
        #open('/sys/class/gpio/gpio60/direction').read()
        print "Trying %s" % tstr
        open(tstr).read()
    except:
        # it isn't, so export it
        print("exporting GPIO %d" %id)
        gpioId = "%d" %id
        open('/sys/class/gpio/export', 'w').write(gpioId)

    open(tstr, 'w').write('in')
    
def cleanGpio(id):
    # cleanup - remove GPIO60 folder from file system
    idStr = "%d" %id
    open('/sys/class/gpio/unexport', 'w').write(idStr)

def readGpio(id):
    gpioStr = "/sys/class/gpio/gpio%d" % id
    gpioVal = gpioStr + "/value"
    tstr = "%s" %gpioVal
    red = open(tstr).read()
    return red.rstrip()
    
#if readIt:
#    trigger = 0
#    red = open('/sys/class/gpio/gpio60/value').read()
#    comp = red.rstrip()
#    lastVal = comp
#    while 1:
#        red = open('/sys/class/gpio/gpio60/value').read()
#        comp = red.rstrip()
#
#        if(lastVal == comp) :
#            #do nothing
#            dummy = 1    
#        else :
#            trigger = 1
#            lastVal = comp
#
#        if trigger==1 :
#            if(comp== '1'):
#                #print "gottit"
#                gpioHiCnt += 1
#                gpioHiLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#            else:
#                gpioLoCnt += 1
#                gpioLoLast = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#
#
#
#        mstr = "Lo::P9_12, %d, " % gpioLoCnt
#        mstr += gpioLoLast
#        #mstr += lastLoTime
#        #print mstr.strip()
#        mstr += "Hi::P9_12, %d, " % gpioHiCnt
#        mstr += gpioHiLast
#        #mstr += lastHiTime
#        print mstr.strip()
#
#        #print red
#        #mstr = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#        #mstr += red.rstrip()
#        #mstr += (" %d" % gpioHiCnt)
#        #mstr += (" %d" % gpioLoCnt)
#        #print mstr
#        time.sleep(1)

        
#initalize all last vals
def initLoop():
    idx = 0        
    for name in gpio_names:
        if(name == 'nil'):
            #skip unassigned
            dummy = 1
        else:
            gpio_lastVal[idx] = readGpio(idx)
        idx += 1
def loop():
    #for every gpio
    idx = 0
    for name in gpio_names:
        if(name == 'nil'):
            #skip unassigned
            dummy = 1
        else:
            comp = readGpio(idx)
            #print "%d::%s" % (idx, name)
            if(gpio_lastVal[idx] != comp):
                gpio_trigger[idx] = 1
                gpio_lastVal[idx] = comp

            if(gpio_trigger[idx]):
                if(comp== '1'):
                    gpio_HiCnt[idx] += 1
                    gpio_LastHiTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                else:
                    gpio_LoCnt[idx] += 1
                    gpio_LastLoTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

                mstr = "%d::%s, %d, " %(idx, gpio_names[idx], gpio_LoCnt[idx])
                mstr += gpio_LastLoTime[idx]
                mstr += ", %d, " %(gpio_HiCnt[idx])
                mstr += gpio_LastHiTime[idx]
                print mstr.strip()
                
        idx += 1 #idx for for loop



openGpioForRead(60)
openGpioForRead(112)
openGpioForRead(115)

initLoop()
while(1):
	loop()
	time.sleep(2)
	


r115 = readGpio(115)

print "r115 %s" %r115
cleanGpio(115)
