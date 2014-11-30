#!/usr/bin/python


#array_names 
#eg:
#gpio_names[60] = "P9_12"


#open gpio for reading
def openGpioForRead(id):
    gpioStr = "/sys/class/gpio/gpio%d" % id
    gpioDir = gpioStr + "/direction"
    print type(gpioDir)
    print gpioDir
    print gpioStr

    tstr = "%s" %gpioDir
    print "TSTR:"
    # check to see if the pin is already exported
    tstr = r'/sys/class/gpio/gpio60/direction' 
    tstr = r'test.test'
    print "TSTR:__%s__" %tstr
    f = open(tstr).read()

    tstr = "tmp/tmp"
    tstr = r'/sys/class/gpio/gpio60/direction' 

    #f = open(tstr).read()

    #print f
    try:
        #open('/sys/class/gpio/gpio60/direction').read()
        #open('test.test').read()
        open(tstr).read()
    except:
        # it isn't, so export it
        print("exporting GPIO 60")
        #open('/sys/class/gpio/export', 'w').write('60')
    
#        
#    # set Port 8 Pin 3 for output    
#    if readIt:
#        open('/sys/class/gpio/gpio60/direction', 'w').write('in')
#    else:
#        open('/sys/class/gpio/gpio60/direction', 'w').write('out')
#        open('/sys/class/gpio/gpio60/value', 'w').write('1')



openGpioForRead(60)
