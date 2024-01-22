# pygl50_evo
Python script for downloading measurements from a Beurer GL50 EVO glucose meter

Download measurements from Beurer GL50 EVO using an ESP32 and Bluetooth Low Energy (BLE)

With this device one can use either a PC app (Windows) via USB, or an Android app that uses Bluetooth Low Energy (Beurer Health Manager). The later downloads measurements from the device and displays graphs. Measurements are stored locally on the smartphone, and can be displayed.

This project is a complement to a [previous one](https://github.com/N0ury/ESP32-GL50_EVO-BLE) that uses ESP32 BLE Arduino library.

I wanted to download GL50 EVO data using a Macbook.
With this script no need to use an ESP32.
It can be used on Linux, MacOS, or Windows.
It uses Bluetooth Low Energy.
It is written in Python.
  
Don't forget to modify the  
```
    "ED:AC:3E:EA:54:FF"
    if platform.system() != "Darwin"
    else "2ACAC34E-A163-F72E-30B7-963F16F6E7E1"
```
lines to suit your situation.  

Lines 18 to 25 can be safely removed. 
I wanted to harmonize the codes with another blood glucose meter.
