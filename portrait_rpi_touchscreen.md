Description|Command
------------ | -------------
Install xinput|`sudo apt-get install xinput`
Rotate the display by editing config.txt|`sudo nano /boot/config.txt`
...add this to the buttom of the file|`display_rotate=1 Use Ctrl X, Yes to Save`
Create a script to rotate the touchscreen|`nano /home/pi/touch_rotate.sh`
...add the following lines|#!/bin/sh
`xinput --set-prop 'FT5406 memory based driver' 'Coordinate Transformation Matrix'  0 1 0 -1 0 1 0 0 1`
Make the script executable|`chmod +x touch_rotate.sh`
Make the script run when the GUI starts by editing autostart|`sudo nano ~/.config/lxsession/LXDE-pi/autostart`
...add this to the bottom to run your script|`@/home/pi/touch_rotate.sh`
Reboot|`sudo reboot`
