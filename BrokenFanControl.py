#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

# ask smcFanControl for processor temps TC0D and TC0D smc keys, get 4th workfrom output and convert to a decimal integer
# Sample output is '  TC0D  [sp78]  (bytes 34 60)'
appcall = "/Applications/smcFanControl.app/Contents/Resources/smc "
readsensorscall = appcall + "-r -k "
setfancall = appcall + "-k F0Mx -w "
temp1 = int(subprocess.check_output(readsensorscall + "TC0D", shell=True, stderr=subprocess.PIPE).split()[3], 16)
temp2 = int(subprocess.check_output(readsensorscall + "TC0P", shell=True, stderr=subprocess.PIPE).split()[3], 16)
actualfanspeed = int(subprocess.check_output(readsensorscall + "F0Ac", shell=True, stderr=subprocess.PIPE).split()[2])
# print "%d°, %d°, %drpm" % (temp1, temp2, actualfanspeed)
# now set fan speed according to processor temp
if temp1 < 50:
    fanspeed = 1800
elif temp1 < 58:
    fanspeed = 2500
elif temp1 < 62:
    fanspeed = 3000
elif temp1 < 66:
    fanspeed = 3600
elif temp1 < 70:
    fanspeed = 4200
elif temp1 < 75:
    fanspeed = 5000
else:
    fanspeed = 6500
# print "Calling %s" % setfancall + hex(fanspeed << 2)[2:]
subprocess.call(setfancall + hex(fanspeed << 2)[2:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print "Get back %s (%d)" % (hex(fanspeed << 2), fanspeed)
