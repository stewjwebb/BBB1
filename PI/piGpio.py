#!/usr/bin/python2

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while (1):
   input_value = GPIO.input(3)
   print input_value


#import time
#from time import gmtime, strftime
##gpio_names[gpioId] = "name" 
##eg:
##gpio_names[60] = "P9_12"
##gpio_trigger[gpioId] = 0/1
##gpio_LoCnt[gpioId] = 0
##gpio_HiCnt[gpioId] = 0
#
#
#gpio_names = ["nil" for i in range(256)] #i think there are 141 gpios
#gpio_trigger = [0 for i in range(256)]
#gpio_LoCnt = [0 for i in range(256)]
#gpio_HiCnt = [0 for i in range(256)]
#gpio_LastHiTime = ["nil" for i in range(256)]
#gpio_LastLoTime = ["nil" for i in range(256)]
#gpio_lastVal = [-1 for i in range(256)]
#
#
#
#
###In the following table, starting with ## means not available
##PIN 37 HEADER P8_08 GPIONUM 67 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 39 HEADER P8_09 GPIONUM 69 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 38 HEADER P8_10 GPIONUM 68 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 13 HEADER P8_11 GPIONUM 45 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 12 HEADER P8_12 GPIONUM 44 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 9 HEADER P8_13 GPIONUM 23 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 10 HEADER P8_14 GPIONUM 26 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 15 HEADER P8_15 GPIONUM 47 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 14 HEADER P8_16 GPIONUM 46 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 11 HEADER P8_17 GPIONUM 27 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 35 HEADER P8_18 GPIONUM 65 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 8 HEADER P8_19 GPIONUM 22 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
###PIN 33 HEADER P8_20 GPIONUM 63 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 32 HEADER P8_21 GPIONUM 62 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 5 HEADER P8_22 GPIONUM 37 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 4 HEADER P8_23 GPIONUM 36 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
##PIN 31 HEADER P8_26 GPIONUM 61 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
###PIN 56 HEADER P8_27 GPIONUM 86 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 58 HEADER P8_28 GPIONUM 88 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 57 HEADER P8_29 GPIONUM 87 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN 59 HEADER P8_30 GPIONUM 89 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN VDD_5V HEADER P9_05 GPIONUM Current 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
###PIN VDD_5V HEADER P9_06 GPIONUM Current 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
##PIN 28 HEADER P9_11 GPIONUM 30 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
##PIN 30 HEADER P9_12 GPIONUM 60 55 Fixnum 7 GPIO pullIsEnabled pullUppp fastSlew
##PIN 16 HEADER P9_15 GPIONUM 48 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
##PIN 87 HEADER P9_17 GPIONUM 5 39 Fixnum 7 GPIO pullIsEnabled pullDown fastSlew
#
#gpio_names[67] = "P8_08" ##PIN 37
#gpio_names[69] = "P8_09" ##PIN 39
#gpio_names[68] = "P8_10" ##PIN 38
#gpio_names[45] = "P8_11" ##PIN 13 <----DIDN'T WORK
#gpio_names[44] = "P8_12" ##PIN 12 <----DIDN'T WORK
#gpio_names[23] = "P8_13" ##PIN 9   <----DIDN'T WORK
#
#
#gpio_names[26] = "P8_14" ##PIN 10<----DIDN'T WORK
#gpio_names[47] = "P8_15" ##PIN 15<----DIDN'T WORK
#gpio_names[46] = "P8_16" ##PIN 14<----DIDN'T WORK
#gpio_names[27] = "P8_17" ##PIN 11<----DIDN'T WORK
#gpio_names[65] = "P8_18" ##PIN 35<----DIDN'T WORK
#gpio_names[22] = "P8_19" ##PIN 8<----DIDN'T WORK
#
#gpio_names[61] = "P8_26" ##PIN 31
#
#gpio_names[30] = "P9_11" ##PIN 28
#gpio_names[60] = "P9_12" ##PIN 30
#gpio_names[48] = "P9_15" ##PIN 16
#gpio_names[5] = "P9_17" ##PIN 87<----DIDN'T WORK???
#
#
#
#
#def openGpioForRead(id):
#    gpioStr = "/sys/class/gpio/gpio%d" % id
#    gpioDir = gpioStr + "/direction"
#
#    tstr = "%s" %gpioDir
#
#    try:
#        #open('/sys/class/gpio/gpio60/direction').read()
#        print "Trying %s" % tstr
#        open(tstr).read()
#    except:
#        # it isn't, so export it
#        print("exporting GPIO %d" %id)
#        gpioId = "%d" %id
#        open('/sys/class/gpio/export', 'w').write(gpioId)
#
#    open(tstr, 'w').write('in')
#    
#def cleanGpio(id):
#    # cleanup - remove GPIO#{id} folder from file system
#    idStr = "%d" %id
#    open('/sys/class/gpio/unexport', 'w').write(idStr)
#
#def readGpio(id):
#    gpioStr = "/sys/class/gpio/gpio%d" % id
#    gpioVal = gpioStr + "/value"
#    tstr = "%s" %gpioVal
#    red = open(tstr).read()
#    return red.rstrip()
#    
#        
#def cleanLoop():
#    idx = 0        
#    for name in gpio_names:
#        if(name == 'nil'):
#            #skip unassigned
#            dummy = 1
#        else:
#            cleanGpio(idx)
#        idx += 1
#
##initalize all last vals
#def initLoop():
#    idx = 0        
#    for name in gpio_names:
#        if(name == 'nil'):
#            #skip unassigned
#            dummy = 1
#        else:
#            openGpioForRead(idx)
#            gpio_lastVal[idx] = readGpio(idx)
#        idx += 1
#def loop():
#    #for every gpio
#    newline = 0
#    idx = 0
#    for name in gpio_names:
#        if(name == 'nil'):
#            #skip unassigned
#            dummy = 1
#        else:
#            comp = readGpio(idx)
#            #print "%d::%s" % (idx, name)
#            if(gpio_lastVal[idx] != comp):
#                gpio_trigger[idx] = 1
#                gpio_lastVal[idx] = comp
#
#            if(gpio_trigger[idx]):
#                if(comp== '1'):
#                    gpio_HiCnt[idx] += 1
#                    #gpio_LastHiTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#                    gpio_LastHiTime[idx] = "%f" %(time.time())
#                else:
#                    gpio_LoCnt[idx] += 1
#                    #gpio_LastLoTime[idx] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#                    gpio_LastLoTime[idx] = "%f" %(time.time())
#
#                mstr = "%03d, %s, LO, %d, " %(idx, gpio_names[idx], gpio_LoCnt[idx])
#                mstr += gpio_LastLoTime[idx]
#                mstr += ", HI, %d, " %(gpio_HiCnt[idx])
#                mstr += gpio_LastHiTime[idx]
#                mstr += ";"
#                print mstr.strip()
#                newline = 1
#                
#        idx += 1 #idx for for loop
#    if(newline==1):
#        print ""
#
#
#
#
#initLoop()
#while(1):
#    loop()
#    time.sleep(2)
#        
#cleanLoop()
##cleanGpio(115)
