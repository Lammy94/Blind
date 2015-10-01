#import command line 
import sys

#read variable from command line
var = str(sys.argv[1])

#print the wait time
print ("window is" + var)

#open desire file
target = open("blind/desired.txt", 'w')

#write variable to file
target.write(var)

#close the file 
target.close()
