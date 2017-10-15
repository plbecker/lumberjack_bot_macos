from pyautogui import *
from time import sleep
import struct
import operator
import Quartz.CoreGraphics as CG
import sys, getopt
from pykeyboard import PyKeyboard

k = PyKeyboard()

class ScreenPixel(object):
    def pixel(self, x, y):
        region = CG.CGRectMake(x, y, 1, 1)
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)

        prov = CG.CGImageGetDataProvider(image)
        self._data = CG.CGDataProviderCopyData(prov)
        self.width = CG.CGImageGetWidth(image)
        self.height = CG.CGImageGetHeight(image)
        data_format = "BBBB"
        b, g, r, a = struct.unpack_from(data_format, self._data, offset=0)
        return (r, g, b)

def move(_pos, _now):
    if _pos == 'left' and _now == 'left':
        k.tap_key('left')
        sleep(0.0162)
        k.tap_key('left')
    elif _pos == 'left' and _now == 'right':
        k.tap_key('right')
        sleep(0.0162)
        k.tap_key('right')
    elif _pos == 'right' and _now == 'right':
        k.tap_key('right')
        sleep(0.0162)
        k.tap_key('right')
    elif _pos == 'right' and _now == 'left':
        k.tap_key('left')
        sleep(0.0162)
        k.tap_key('left')

#width, height = size()
#print(width, height)
width = 360
height = 900
width *= 2
height *= 2
moveTo(333, 1040)

posY = [790, 690, 590, 490, 390, 290]
posX = [250, 350]

q = ['left', 'left', 'left']

sp = ScreenPixel()

l0 = sp.pixel(posX[0], posY[0])
l1 = sp.pixel(posX[0], posY[1])
l2 = sp.pixel(posX[0], posY[2])

r0 = sp.pixel(posX[1], posY[0])
r1 = sp.pixel(posX[1], posY[1])
r2 = sp.pixel(posX[1], posY[2])

if l0[0] == 154 and l0[1] == 117 and l0[2] == 66:
    q[0] = 'right'
    pos = 'right'
else:
    pos = 'left'
if l1[0] == 154 and l1[1] == 117 and l1[2] == 66:
    q[1] = 'right'
if l2[0] == 154 and l2[1] == 117 and l2[2] == 66:
    q[2] = 'right'

qlen = 3

while True:
    if qlen == 3:
        now = q[0]
        move(pos, now)
        now = q[1]
        move(pos, now)
        now = q[2]
        move(pos, now)
        qlen = 0
    elif qlen == 0:
        movements = []

        l = []
        for i in range(0,5):
            l.append(sp.pixel(posX[0], posY[i]))

        r = []
        for o in range(0,5):
            r.append(sp.pixel(posX[1], posY[o]))

        for t in range(0,5):
            if l[t][0] == 154 and l[t][1] == 117 and l[t][2] == 66:
                movements.append('right')
            else:
                movements.append('left')
        #print("next movements", movements)
        for x in range(0,5):
            now = movements[x]
            move(pos, now)

    click()
    sleep(0.067)

