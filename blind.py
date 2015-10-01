#COUNT AND FILE READER STARTUP!!!
import time
wait = 0
from motorcontrol import clockwise
from motorcontrol import counterclock

def readMin():
  #read minimum file
  fo = open('blind/min.txt','r')
  minimum = fo.read()
  fo.close()
  minimum = int(minimum)
  return minimum

def readMax():
  #read maximum file
  fo = open('blind/max.txt','r')
  maximum = fo.read()
  fo.close()
  maximum = int(maximum)
  return maximum

def readCurrent():
  #read current file
  fo = open('blind/current.txt','r')
  current = fo.read()
  fo.close
  current = int(current)
  return current

def readDesired():
  #read desired file
  fo = open('blind/desired.txt','r')
  desired = fo.read()
  fo.close
  desired = int(desired)
  return desired

def readWait():
  #read time to wait
  fo = open('blind/wait.txt','r')
  waitTime = fo.read()
  fo.close
  waitTime = int(waitTime)
  return waitTime

def writeCurrent():
  fo = open('blind/current.txt','r+')
  current = fo.write(s)
  fo.close


waitTime = readWait()
current = readCurrent()
print current
time.sleep(waitTime/10)

#-------------------------------------------------------------------------------
#start loop
while True:
  minimum = readMin()
  maximum = readMax()
  current = readCurrent()
  desire = readDesired()
  waitTime = readWait()
  
  while (desire != current):
    #check if current position is lower than desired
    if(desire > current):

      wait = 0
      print ("clockwise")

      #move
      clockwise()
      
      #add to current
      current = current + 1

      #write new position to file
      s = str(current)
      writeCurrent()

      #output position and direction
      print ("position: " + s + " - counter clockwise")

      #wait some time
      time.sleep(waitTime/10)

    #check if current position is higher than desired
    elif (desire < current):

      wait = 0
      #move
      counterclock()
      
      #add to current
      current = current - 1      

      #write new position to file
      s = str(current)
      writeCurrent()

      #output position and direction
      print ("position: " + s + " - counter clockwise")

      #wait some time
      time.sleep(waitTime/10)
      
    current = readCurrent()
    desire = readDesired()
    
    

    #if the current position is the same as desired, do nothing and wait. 
  while (desire == current):
    wait = str(wait)
    print ('waiting #' + wait)
    wait = int(wait)
    wait = wait + 1
    time.sleep(waitTime * 10)
    current = readCurrent()
    desire = readDesired()
