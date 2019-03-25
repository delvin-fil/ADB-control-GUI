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
from adb.client import Client as AdbClient

warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, '')
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
PIPE = subprocess.PIPE

dev = subprocess.Popen(
    "adb devices| awk '/device$/{if (NR!=1) {print $1}}'",
    stderr=None,
    stdout=PIPE,
    shell=PIPE)
dev = str(dev.stdout.read())
dev = re.sub(r'b\'|\\n\'', r'', dev)

pygame.init()

size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ADB control')
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

icon_surf = pygame.image.load(path + '/android.png')
pygame.display.set_icon(icon_surf)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            mousepos = str(mousepos[0]) + ' ' + str(mousepos[1])
            print (f"input tap {mousepos}")
            device.shell(f"input tap {mousepos}")
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device(f"{dev}")
    result = device.screencap()
    img = pygame.image.load(io.BytesIO(result))
    screen.blit(img, (0, 0))
    clock.tick(20)
    pygame.display.flip()
