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

#PIN 39 HEADER P8_09 23 Fixnum 7 GPIO pullIsEnabled pullUppp slowSlew
#PIN 33 HEADER P8_20 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 32 HEADER P8_21 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 5 HEADER P8_22 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 4 HEADER P8_23 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 56 HEADER P8_27 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 58 HEADER P8_28 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 57 HEADER P8_29 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 59 HEADER P8_30 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN VDD_5V HEADER P9_05 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN VDD_5V HEADER P9_06 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 30 HEADER P9_12 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
#PIN 29 HEADER P9_13 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew

gpio_names[60] = "P9_12"
gpio_names[48] = "P9_15"
gpio_names[115] = "P9_27"
gpio_names[39] = "P8_09"
gpio_names[33] = "P8_20"
gpio_names[32] = "P8_21"
gpio_names[5] = "P8_22"
gpio_names[4] = "P8_23"
#gpio_names[56] = "P8_27"
gpio_names[58] = "P8_28"
gpio_names[57] = "P8_29"
#gpio_names[59] = "P8_30"
gpio_names[30] = "P9_12"
gpio_names[29] = "P9_13"

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
    # cleanup - remove GPIO#{id} folder from file system
    idStr = "%d" %id
    open('/sys/class/gpio/unexport', 'w').write(idStr)

def readGpio(id):
    gpioStr = "/sys/class/gpio/gpio%d" % id
    gpioVal = gpioStr + "/value"
    tstr = "%s" %gpioVal
    red = open(tstr).read()
    return red.rstrip()
    
        
def cleanLoop():
    idx = 0        
    for name in gpio_names:
        if(name == 'nil'):
            #skip unassigned
            dummy = 1
        else:
            cleanGpio(idx)
        idx += 1

#initalize all last vals
def initLoop():
    idx = 0        
    for name in gpio_names:
        if(name == 'nil'):
            #skip unassigned
            dummy = 1
        else:
            openGpioForRead(idx)
            gpio_lastVal[idx] = readGpio(idx)
        idx += 1
def loop():
    #for every gpio
    newline = 0
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
                    #gpio_LastHiTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                    gpio_LastHiTime[idx] = "%f" %(time.time())
                else:
                    gpio_LoCnt[idx] += 1
                    #gpio_LastLoTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                    gpio_LastLoTime[idx] = "%f" %(time.time())

                mstr = "%03d, %s, LO, %d, " %(idx, gpio_names[idx], gpio_LoCnt[idx])
                mstr += gpio_LastLoTime[idx]
                mstr += ", HI, %d, " %(gpio_HiCnt[idx])
                mstr += gpio_LastHiTime[idx]
                mstr += ";"
                print mstr.strip()
                newline = 1
                
        idx += 1 #idx for for loop
    if(newline==1):
        print ""




initLoop()
while(1):
    loop()
    time.sleep(2)
        
#cleanLoop()
cleanGpio(115)
