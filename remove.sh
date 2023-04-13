#! /bin/bash

echo "click on galerie"
adb shell input tap 80.9 477.6

sleep 5
echo "click on 1st media"
adb shell input tap 32 161.8

sleep 5
echo "click on trash"
adb shell input tap 592 97
sleep 1
echo "click on trash"
adb shell input tap 592 97

sleep 5
echo "click on popup yes"
adb shell input tap 499.2 678.5

sleep 5
echo "clicking on task viewer"
adb shell input tap 566.2 1208.0
sleep 1
adb shell input tap 566.2 1208.0

sleep 5
echo "flushin ram"
adb shell input swipe 578.2 1046.1 80.9 1113.0 500
