*BrokenFanControl* is a simple program to set the _maximum_ fan speed in a Mac Mini.

Introduction
------------
It's not useful for everyone and can be dangerous for your computer. I needed it because I broke a temperature sensor in my Mac Mini Server (Mid-2010) changing one of the internal drive for a Crucial m4 (a great drive, btw). Therefore the fan was always starting at full speed and this was _really_ annoying.

All fan control programs are designed to raise the minimum fan speed to cool more while my problem is the opposite: lower fan speed (allowing the computer to raise its temp). So I decided to run my own (working on what have been already done by others).

WARNINGS
--------
This program is not for end-users. It is for _hackers_, people that know their Mac and are not afraid of it, people that know how to start up and use the terminal (and, again, are not afraid of it).

BrokenFanControl is dangerous. Setting the maximum fan speed effectively inhibit the cooling of the computer. *This is dangerous*, can broke your computer or set it to fire!

I wrote it because I have problems (broken HD sensor, as said before) it should not be run on a working system!

The program has been tested _only_ on a Mid-2010 Mac Mini (server edition, the one with 2 disk drives). Should work on any Mac Mini intel but I'm not sure of that. Please make your tests before install!

The script requires python 2.7+, that's the default on Lion and Mountain Lion, can be installed for previous OS X versions.

The code
--------
Is very simple: it simply reads, via smcFanControl command line program, the values of TC0D (the processor temperature) and set the maximum speed of the fan (F0Mx) also via smcFanControl. The fan speed goes from 1800 when the CPU temp is 50°C or less to the maximum speed when the temp is over 75°C.

The commented print statement are for debug and use also TC0P (probably the CPU heatsink) and F0Ac (the current fan speed).

How to test it without burning your Mac
---------------------------------------
My code is a simple python script that wraps some call to the command line component of smcFanControl.

Before installing it, test it uncommenting the print statements and commenting the last subprocess.call call (the one that sets the maximum speed). If fans behave strangely: stop the computer, wait a little and wake it. All should be normal.

Installation
------------
The script is installed so that it's called by cron every minute and by SleepWatcher at wake up time (so you don't have to hear full speed fans for a full minute when the mini wakes up).

Follow the instructions. The instructions are not very easy to follow. This is intentional. If you don't understand them, well, you should not use this script. As said before: it's dangerous. :)

* download [smcFanControl](http://www.eidac.de/) and install it in /Application
* copy BrokenFanControl.py in /usr/local/bin and make it executable
* download [SleepWatcher](http://www.bernhard-baehr.de/) and install it
* * Assuming you've downloaded it in Desktop
* * `sudo mkdir -p /usr/local/sbin /usr/local/share/man/man8`
* * `sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher /usr/local/sbin`
* * `sudo cp ~/Desktop/sleepwatcher_2.2/sleepwatcher.8 /usr/local/share/man/man8`
* `copy de.bernhard-baehr.sleepwatcher-BrokenFan.plist to /Library/LaunchDaemons`
* `sudo launchctl load /Library/LaunchDaemons/de.bernhard-baehr.sleepwatcher-BrokenFan.plist`
* `sudo crontab -e`
* * insert the line below (from */1 to end of line)
* * `*/1 * * * * /usr/local/sbin/smcFanReset`
* Enjoy the silence.

