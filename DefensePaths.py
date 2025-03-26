import math, random
from direct.showbase.Loader import *
from panda3d.core import NodePath
from panda3d.core import Vec3

def Cloud(radius = 1):
    # making the defense path shaped like a cloud
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec * radius

def BaseballSeams(step, numSeams, B, F=1):
    # making the defense path shaped like baseball seams
    time = step / float(numSeams) * 2 * math.pi
    F4 = 0
    R = 1
    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)
    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)

    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    return Vec3(x, y, z)

def CircleX(t):
    # making a defense path that changes its y and z positions (and also doesn't want to cooperate)
    x = 0.0 * math.cos(t)
    y = 50.0 * math.sin(t)
    z = 50.0 * math.tan(t)

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec

def CircleY(t):
    # making a defense path that changes its x and z positions 
    x = 50.0 * math.cos(t)
    y = 0.0 * math.sin(t)
    z = 50.0 * math.tan(t)

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec

def CircleZ(t):
    # making a defense path that changes its x and y positions
    x = 50.0 * math.cos(t)
    y = 50.0 * math.sin(t)
    z = 0.0 * math.tan(t)

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec