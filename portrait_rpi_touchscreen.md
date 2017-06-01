1. Install xinput: `sudo apt-get install xinput`
2. Rotate the display by editing config.txt: `sudo nano /boot/config.txt`
.. add this to the buttom of the file: `display_rotate=1 Use Ctrl X, Yes to Save`
3. Create a script to rotate the touchscreen: `nano /home/pi/touch_rotate.sh`
.. add the following command: `xinput --set-prop 'FT5406 memory based driver' 'Coordinate Transformation Matrix'  0 1 0 -1 0 1 0 0 1`
4. Make the script executable: `chmod +x touch_rotate.sh`
5. Make the script run when the GUI starts by editing autostart: `sudo nano ~/.config/lxsession/LXDE-pi/autostart`
.. add this to the bottom to run your script: `@/home/pi/touch_rotate.sh`
6. Reboot: `sudo reboot`
