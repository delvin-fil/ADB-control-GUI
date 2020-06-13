# ADB control
ADB GUI control Android devices
Последняя рабочая версия ADB-control-GUI.py. Добавлена возможность ввода с клавиатуры.

Необходимое:<br>
python3.6, adb<br>
Используемые модули:<br>
pygame, warnings, locale, sys, io, re, image, subprocess, inspect, os.path<br>

![Screenshot](/screenshot.png)

Настройка:<br>
	adb tcpip 5555<br>
	adb connect 192.168.0.14:5555<br>
	sudo adb devices<br>
Если не планируется использовать WiFi, то в строке 23 файла control.py указываем имя Вашего устройства.

