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
gpio_names[48] = "P9_15"
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
