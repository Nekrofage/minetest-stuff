__author__ = '@damianmooney'
"""
    Sphere via pythagoras
"""
import math
from mcpi import minecraft as minecraft
from mcpi import block as block


def get_distance(pos1, pos2):
    """ calculate the distance between 2 points """

    distance = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2])**2)
    return distance


mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()

myx = int(playerPos.x) - 24
myy = int(playerPos.y) + 2
myz = int(playerPos.z) - 24

cubesize = 31  # pick an odd number
rad = ((cubesize/2) + 1)
centre_sq = (myx + rad, myy + rad, myz + rad)

#  make a large block
mc.setBlocks(myx, myy, myz, myx + cubesize, myy + cubesize, myz + cubesize, block.GLASS)

for x in range(cubesize + 1):
    for y in range(cubesize + 1):
        for z in range(cubesize + 1):
            check_sq = (myx + x, myy + y, myz + z)
            dist = get_distance(centre_sq, check_sq)
            if dist > rad:  # carve a sphere
                mc.setBlock(myx + x, myy + y, myz + z, block.AIR)
            if dist < (rad - 3):  # hollow it out
                mc.setBlock(myx + x, myy + y, myz + z, block.WATER_FLOWING)

