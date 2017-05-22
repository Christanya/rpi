#!/usr/bin/python

# user settings
debug = True

from subprocess import call
from sense_hat import SenseHat
import time
sense = SenseHat()
import socket 
import fcntl
import struct

# need to remember where I got this get_ip_address routine
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# set host name
thishost = get_ip_address('wlan0')

# set message to display
print "\n WLAN0 IP for \"" + socket.gethostname() + "\" is " + thishost
print " NOTE: Use Sense Hat stick (any direction) to stop after next scroll..."

# 
# display message
count = 0
while (count == 0):
  sense.clear()
  sense.show_message(thishost,0.1,[255,255,0],[0,0,255])
  chkStick = sense.stick.get_events()
  if (chkStick != []):
    count = 1

sense.clear()
