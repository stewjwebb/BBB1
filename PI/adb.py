import time
import os


androidPath = "/sdcard/"
def push(fromfile, tofile=None ):
   if(tofile==None):
      #`adb push #{fromfile} #{@androidPath}#{fromfile}`
      cmd = "adb push %s %s%s" %(fromfile, androidPath, fromfile)
      #print cmd
      stream = os.popen(cmd).read()
      print stream

def pull (fromfile, tofile=None):
   if(tofile==None):
      #`adb pull #{@androidPath}#{fromfile}`
      cmd = "adb pull %s%s" %(androidPath, fromfile)
   else:
      cmd = "adb pull %s%s %s" %(androidPath, fromfile, tofile)
   #print cmd
   stream = os.popen(cmd).read()
   print stream

def lstxt ():
   #lsr = `adb shell ls -l /sdcard/*.txt`
   stream = os.popen("adb shell ls -l /sdcard/*.txt").read()
   print stream

def ls (file):
   #lsr = `adb shell ls -l #{@androidPath}#{file}`
   cmd = "adb shell ls -l %s%s" %(androidPath, file)
   #print cmd
   stream = os.popen(cmd).read()
   print stream
	

def rm (file):
   #`adb shell rm #{@androidPath}#{file}`
   cmd = "adb shell rm %s%s" %(androidPath, file)
   #print cmd
   stream = os.popen(cmd).read()
   print stream

def touch(file):
   #`adb shell touch #{@androidPath}#{file}`
   cmd = "adb shell touch %s%s" %(androidPath, file)
   #print cmd
   stream = os.popen(cmd).read()
   print stream

def timeStamp(file):
   #`echo #{tt} > #{file}` 
   tt = time.time()
   cmd = "echo %f > %s" %(tt, file)
   #print cmd
   stream = os.popen(cmd).read()
   print stream
	

cnt=0
while(cnt<5):
   active_f = "act_%d.txt" %(cnt)
   block_f = "block_%d.txt" %(cnt)
   touch(block_f)
   #generate result
   timeStamp(active_f)   
   #copy result to phone
   push(active_f)
   lstxt()
   #remove block file
   rm(block_f)
   cnt += 1

