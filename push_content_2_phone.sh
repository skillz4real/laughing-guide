#! /bin/bash

echo "pushing files"
sleep 5
adb push /home/ftpuser/whacontent/* /sdcard/DCIM/Camera/


mv /home/ftpuser/whacontent/* /home/ftpuser/whacontent.old/