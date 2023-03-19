#! /bin/bash

echo "clicking on file btn"
adb shell input tap 71 382

sleep 5
echo "filtering by image"
adb shell input tap 61 182

sleep 5
echo "filtering by video"
adb shell input tap 287 189

sleep 5
echo "clicking on option btn(...)"
adb shell input tap 466 66

sleep 5
echo "clicking on select all opt"
adb shell input tap 355 220

sleep 5
echo "clicking on share (opens wha)"
adb shell input tap 356 59

sleep 5
echo "clicking on status"
adb shell input tap 94 138

sleep 5
echo "clicking on arrow bottom right of screen"
adb shell input tap 464 861

sleep 5
echo "clicking on arrow"
adb shell input tap 464 861

sleep 5
echo "clicking on square"
adb shell input tap 388 923

sleep 5
echo "swiping up to apps (clearing ram)"
adb shell input swipe 267 740 267 51 500

echo "Done"
