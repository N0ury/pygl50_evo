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
if (advertisedDevice->haveName() && advertisedDevice->getName() == "Beurer GL50EVO" && advertisedDevice->getAddress().toString() == "ed:ac:3e:ea:54:ff")
```
line to suit your situation.  
