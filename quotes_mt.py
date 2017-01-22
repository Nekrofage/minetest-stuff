__author__ = '@damianmooney'
"""
 code to write letter shaped blocks in minetest with
 fantastic raspberryjammod by Alexander Pruss
 should also play nice with minecraft-pi edition
"""

import string
from mc import *
import time

def do_a():
    let =	[
     ' xx ',
     'x  x',
     'xxxx',
     'x  x',
     'x  x']
    return let


def do_b():
    let =	[
     'xxx ',
     'x  x',
     'xxx ',
     'x  x',
     'xxx ']
    return let


def do_c():
    let =	[
     'xxxx',
     'x   ',
     'x   ',
     'x   ',
     'xxxx']
    return let


def do_d():
    let =	[
     'xxx ',
     'x  x',
     'x  x',
     'x  x',
     'xxx ']
    return let


def do_e():
    let =	[
     'xxxx',
     'x   ',
     'xxxx',
     'x   ',
     'xxxx']
    return let


def do_f():
    let =	[
     'xxxx',
     'x   ',
     'xxxx',
     'x   ',
     'x   ']
    return let


def do_g():
    let =	[
     'xxxx ',
     'x    ',
     'x  xx',
     'x   x',
     'xxxx ']
    return let


def do_h():
    let =	[
     'x  x',
     'x  x',
     'xxxx',
     'x  x',
     'x  x']
    return let


def do_i():
    let =	[
     'xxx',
     ' x ',
     ' x ',
     ' x ',
     'xxx']
    return let


def do_j():
    let =	[
     ' xxx',
     '  x ',
     '  x ',
     '  x ',
     'xxx ']
    return let


def do_k():
    let =	[
     'x   x',
     'x  x ',
     'xxx  ',
     'x  x ',
     'x   x']
    return let


def do_l():
    let =	[
     'x   ',
     'x   ',
     'x   ',
     'x   ',
     'xxxx']
    return let


def do_m():
    let =	[
     'xx xx',
     'x x x',
     'x x x',
     'x   x',
     'x   x']
    return let


def do_n():
    let =	[
     'x   x',
     'xx  x',
     'x x x',
     'x  xx',
     'x   x']
    return let


def do_o():
    let =	[
     'xxxx',
     'x  x',
     'x  x',
     'x  x',
     'xxxx']
    return let


def do_p():
    let =	[
     'xxx ',
     'x  x',
     'xxx ',
     'x   ',
     'x   ']
    return let


def do_q():
    let =	[
     'xxxxx',
     'x   x',
     'x   x',
     'x x x',
     'xxxxx']
    return let


def do_r():
    let =	[
     'xxxx ',
     'x   x',
     'xxxx ',
     'x  x ',
     'x   x']
    return let


def do_s():
    let =	[
     'xxxx',
     'x   ',
     'xxxx',
     '   x',
     'xxxx']
    return let


def do_t():
    let =	[
     'xxxxx',
     '  x ',
     '  x ',
     '  x ',
     '  x ']
    return let


def do_u():
    let =	[
     'x  x',
     'x  x',
     'x  x',
     'x  x',
     'xxxx']
    return let


def do_v():
    let =	[
     'x   x',
     'x   x',
     'x   x ',
     ' x x ',
     '  x ']
    return let


def do_w():
    let =	[
     'x   x',
     'x   x',
     'x   x',
     'x x x',
     ' x x ']
    return let


def do_x():
    let =	[
     'x   x',
     ' x x ',
     '  x  ',
     ' x x ',
     'x   x']
    return let


def do_y():
    let =	[
     'x   x',
     'x   x',
     ' xxx ',
     '  x  ',
     '  x  ']
    return let


def do_z():
    let =	[
     'xxxx',
     '  x ',
     ' x  ',
     'x   ',
     'xxxx']
    return let


def do_other():
    let =	[
     ' ',
     ' ',
     ' ',
     ' ',
     ' ']
    return let


def do_comma():
    let =	[
     '  ',
     '  ',
     '  ',
     '  x',
     'x ']
    return let

def do_stop():
    let =	[
     ' ',
     ' ',
     ' ',
     ' ',
     'x']
    return let

def do_quote():
    let =	[
     ' x',
     ' x',
     ' ',
     ' ',
     ' ']
    return let


mc = Minecraft()

playerPos = mc.player.getPos()
myx = int(playerPos.x) - 48
myy = int(playerPos.y) + 8
myz = int(playerPos.z) - 48

xoffset = 0
block_offset = 0
yoffset = 0
initpos = myx, myy, myz
mc.postToChat(initpos)
quotes = []

# read the txt file into a list
f = open('quotes.txt', 'r')
while True:
    buff = f.readline()
    if buff == '':
        break
    quotes.append(buff)
f.close()

for message in quotes:

    debug = open('debug.txt', 'w')
    print(message)
    for i in message:
        xoffset = 0
        if i.isalpha():
            letter = eval('do_%s()' % i.lower())
        elif i in [",", ".", "'"]:  # only do some punc
            if i == ",":
                letter = do_comma()
            if i == ".":
                letter = do_stop()
            if i == "'":
                letter = do_quote()

        else:
            letter = do_other()

        letterw = len(letter[0])
        yoffset = 0
        # print(letterw)
        for row in letter:
            # print(row)
            xoffset = 0
            for j in row:

                if j == 'x':
                    # place a block
                    mc.setBlock(myx + xoffset + block_offset, myy + yoffset, myz, GOLD_BLOCK)
                    # debug.write('%d - %d - %d gold | ' % (myx + xoffset + block_offset, myy + yoffset, myz))
                else:
                    # place air gaps
                    mc.setBlock(myx + xoffset + block_offset, myy + yoffset, myz, AIR)
                    # debug.write('%d - %d - %d air | ' % (myx + xoffset + block_offset, myy + yoffset, myz))

                xoffset += 1
            # debug.write('\n')
            yoffset -= 1
        block_offset += letterw + 1
    time.sleep(5.0)
    # blank out whole line
    mc.setBlocks(myx, myy - 6, myz, myx + xoffset + block_offset, myy, myz, AIR)
    time.sleep(1.0)
    block_offset = 0
    xoffset = 0
    yoffset = 0
debug.close()