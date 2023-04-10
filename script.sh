#! /bin/bash

echo "clicking wha icon"
adb shell input tap 266.6 231.8

sleep 5
echo "clicking on status tab"
adb shell input tap 397.3 238.8

sleep
echo "clicking on camera icon"
adb shell input tap 526.0 1082.1


sleep 5
echo "clicking on media icon"
adb shell input tap 73.9 992.2

sleep 5
echo "clicking on first media"
adb shell input tap 115.8 406.7

sleep 5
echo "sending status update"
adb shell input tap 652 1121

sleep 5
echo "clicking on task viewer"
adb shell input tap 566.2 1208.0

sleep 5
echo "flushing ram"
adb shell input swipe 578.2 1046.1 80.9 1113.0 500

echo "Done"
