# go to whatsapp views menu


# take screenshot
export DATE=$(date)
adb shell screencap -p /sdcard/DCIM/views_${DATE}.png

#go to whatsapp discussion menu


#take screenshot
adb shell screencap -p /sdcard/DCIM/chat_${DATE}.png


#clean


#pull screenshot
cd /home/z/laughing-guide/data/ && adb pull /sdcard/DCIM/*
