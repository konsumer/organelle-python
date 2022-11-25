#!/usr/bin/env python3

from oled_console import OledConsole 
from time import sleep

oled = OledConsole()

oled.setLine(1, 'Hello')
oled.setLine(2, 'World')
oled.setLine(3, 'Hello')
oled.setLine(4, 'World')
oled.setLine(5, 'World')
oled.invertLine(2)

while True:
  oled.draw()
  sleep(0.1)