#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import pygame
import warnings
import locale
import sys
import io
import re
import image
import subprocess
import inspect, os.path
from array import array
from pygame.locals import *

from ppadb.client import Client as AdbClient

#warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, '')
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
print (path)
PIPE = subprocess.PIPE

dev = subprocess.Popen(
    "adb -e devices| awk '/device$/{if (NR!=1) {print $1}}'",
    stderr=None,
    stdout=PIPE,
    shell=PIPE)
dev = str(dev.stdout.read())
dev = re.sub(r'b\'|\\n\'', r'', dev)
#dev = '192.168.0.14:5555'
#dev = 'CLD9BZOV54'
print (dev)
pygame.init()

size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ADB control')

filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

print (path)
#icon_surf = pygame.image.load(path + '/android.png')
icon_surf = pygame.image.load('/home/delvin/codding/adb/android.png')
pygame.display.set_icon(icon_surf)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                os.system('adb -e shell input keyevent 19')
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                os.system('adb -e shell input keyevent 20')
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                os.system('adb -e shell input keyevent 21')
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                os.system('adb -e shell input keyevent 22')
        if event.type == KEYDOWN:
            if event.key == K_MENU:
                os.system('adb -e shell input keyevent 1')
        if event.type == KEYDOWN:
            if event.key == K_HOME:
                os.system('adb -e shell input keyevent 3')
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER:
                os.system('adb -e shell input keyevent 66')
        if event.type == KEYDOWN:
            if event.key == K_0:
                os.system('adb -e shell input keyevent 7')
        if event.type == KEYDOWN:
            if event.key == K_1:
                os.system('adb -e shell input keyevent 8')
        if event.type == KEYDOWN:
            if event.key == K_2:
                os.system('adb -e shell input keyevent 9')
        if event.type == KEYDOWN:
            if event.key == K_3:
                os.system('adb -e shell input keyevent 10')
        if event.type == KEYDOWN:
            if event.key == K_4:
                os.system('adb -e shell input keyevent 11')
        if event.type == KEYDOWN:
            if event.key == K_5:
                os.system('adb -e shell input keyevent 12')
        if event.type == KEYDOWN:
            if event.key == K_6:
                os.system('adb -e shell input keyevent 13')
        if event.type == KEYDOWN:
            if event.key == K_7:
                os.system('adb -e shell input keyevent 14')
        if event.type == KEYDOWN:
            if event.key == K_8:
                os.system('adb -e shell input keyevent 15')
        if event.type == KEYDOWN:
            if event.key == K_9:
                os.system('adb -e shell input keyevent 16')
        if event.type == KEYDOWN:
            if event.key == K_a:
                os.system('adb -e shell input keyevent 29')
        if event.type == KEYDOWN:
            if event.key == K_b:
                os.system('adb -e shell input keyevent 30')
        if event.type == KEYDOWN:
            if event.key == K_c:
                os.system('adb -e shell input keyevent 31')
        if event.type == KEYDOWN:
            if event.key == K_d:
                os.system('adb -e shell input keyevent 32')
        if event.type == KEYDOWN:
            if event.key == K_e:
                os.system('adb -e shell input keyevent 33')
        if event.type == KEYDOWN:
            if event.key == K_f:
                os.system('adb -e shell input keyevent 34')
        if event.type == KEYDOWN:
            if event.key == K_g:
                os.system('adb -e shell input keyevent 35')
        if event.type == KEYDOWN:
            if event.key == K_h:
                os.system('adb -e shell input keyevent 36')
        if event.type == KEYDOWN:
            if event.key == K_i:
                os.system('adb -e shell input keyevent 37')
        if event.type == KEYDOWN:
            if event.key == K_j:
                os.system('adb -e shell input keyevent 38')
        if event.type == KEYDOWN:
            if event.key == K_k:
                os.system('adb -e shell input keyevent 39')
        if event.type == KEYDOWN:
            if event.key == K_l:
                os.system('adb -e shell input keyevent 40')
        if event.type == KEYDOWN:
            if event.key == K_m:
                os.system('adb -e shell input keyevent 41')
        if event.type == KEYDOWN:
            if event.key == K_n:
                os.system('adb -e shell input keyevent 42')
        if event.type == KEYDOWN:
            if event.key == K_o:
                os.system('adb -e shell input keyevent 43')
        if event.type == KEYDOWN:
            if event.key == K_p:
                os.system('adb -e shell input keyevent 44')
        if event.type == KEYDOWN:
            if event.key == K_q:
                os.system('adb -e shell input keyevent 45')
        if event.type == KEYDOWN:
            if event.key == K_r:
                os.system('adb -e shell input keyevent 46')
        if event.type == KEYDOWN:
            if event.key == K_s:
                os.system('adb -e shell input keyevent 47')
        if event.type == KEYDOWN:
            if event.key == K_t:
                os.system('adb -e shell input keyevent 48')
        if event.type == KEYDOWN:
            if event.key == K_u:
                os.system('adb -e shell input keyevent 49')
        if event.type == KEYDOWN:
            if event.key == K_v:
                os.system('adb -e shell input keyevent 50')
        if event.type == KEYDOWN:
            if event.key == K_w:
                os.system('adb -e shell input keyevent 51')
        if event.type == KEYDOWN:
            if event.key == K_x:
                os.system('adb -e shell input keyevent 52')
        if event.type == KEYDOWN:
            if event.key == K_y:
                os.system('adb -e shell input keyevent 53')
        if event.type == KEYDOWN:
            if event.key == K_z:
                os.system('adb -e shell input keyevent 54')

        if event.type == KEYDOWN:
            if event.key == K_COMMA:
                os.system('adb -e shell input keyevent 55')
        if event.type == KEYDOWN:
            if event.key == K_PERIOD:
                os.system('adb -e shell input keyevent 56')
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                os.system('adb -e shell input keyevent 62')
        if event.type == KEYDOWN:
            if event.key == K_EXCLAIM:
                os.system('adb -e shell input keyevent 207')
        if event.type == KEYDOWN:
            if event.key == K_LEFTPAREN:
                os.system('adb -e shell input keyevent 162')
        if event.type == KEYDOWN:
            if event.key == K_RIGHTPAREN:
                os.system('adb -e shell input keyevent 163')
        if event.type == KEYDOWN:
            if event.key == K_MINUS:
                os.system('adb -e shell input keyevent 89')
        if event.type == KEYDOWN:
            if event.key == K_PLUS:
                os.system('adb -e shell input keyevent 81')


        if event.type == MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            mousepos = str(mousepos[0]) + ' ' + str(mousepos[1])
            print (f"input tap {mousepos}")
            device.shell(f"input tap {mousepos}")
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device(f"{dev}")
    result = device.screencap()
    with open('screen.png', 'wb') as fp:
        fp.write(result)
    img = pygame.image.load(io.BytesIO(result))
    #img = pygame.image.load(os.path.join('screen.png'))
    #print (os.path())
    screen.blit(img, (0, 0))
    clock.tick(0.5)
    pygame.display.flip()
#x11vnc -rfbport 5900 -display :0 -dontdisconnect -noxfixes -xdamage -shared -forever -clip 1792x1344+1792+0 -scale 1024x768 -bg -cursor X -o /root/tmp/x11vnc.log -repeat   
