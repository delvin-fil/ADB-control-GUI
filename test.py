#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import pygame
import warnings
import locale
import sys
from pygame.locals import *
from adb.client import Client as AdbClient

warnings.filterwarnings("ignore")
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.0.14:5555")
#device = client.device("CLD9BZOV54")
result = device.screencap()
with open("/home/delvin/codding/games/screenshot.png", "wb") as fp:
	fp.write(result)

warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, '')

pygame.init()

size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption('VNC control')
icon_surf = pygame.image.load('android.png')
pygame.display.set_icon(icon_surf)
clock=pygame.time.Clock()
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
			#print(mousepos)
			device.shell(f"input tap {mousepos}")
	client = AdbClient(host="127.0.0.1", port=5037)
	#device = client.device("CLD9BZOV54")
	device = client.device("192.168.0.14:5555")
	result = device.screencap()
	#print (type(result))
	with open("/home/delvin/codding/games/screenshot.png", "wb") as fp:
		fp.write(result)
	filename = "/home/delvin/codding/games/screenshot.png"
	img=pygame.image.load(filename)
	screen.blit(img,(0,0))			
	clock.tick(20)
	pygame.display.flip()
