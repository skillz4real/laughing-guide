#! /bin/bash

echo "clicking wha icon"
adb shell input tap 266.6 231.8

sleep 5
echo "taking screenshot"
adb shell screencap -p /sdcard/DCIM/Camera/chat_${DATE}.png

sleep 5
echo "clicking on status tab"
adb shell input tap 397.3 238.8

sleep 5
echo "clicking on ..."
adb shell input tap 685 328.7

sleep 5
echo "taking screenshot"
adb shell screencap -p /sdcard/DCIM/Camera/views_${DATE}.png

 sleep 5
echo "clicking on task viewer"
adb shell input tap 566.2 1208.0

sleep 5
echo "flushing ram"
adb shell input swipe 578.2 1046.1 80.9 1113.0 500


#pull screenshot
adb pull /sdcard/DCIM/Camera
