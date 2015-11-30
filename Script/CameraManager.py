import math
import c4d

from c4d import utils
from math import pi

def main():

    obj = op.GetObject()
    object = obj[c4d.ID_USERDATA,1]
    
    if object is None:
        return
    #print object
    
    distance = obj[c4d.ID_USERDATA,2]
    eyeDistance = obj[c4d.ID_USERDATA, 3]
    viewNum = obj[c4d.ID_USERDATA, 4]
    
    current_object = object.GetDown()
    #print distance
    
    objScale = c4d.Vector(1)
    objRot = c4d.Vector()
    
    camDist = (eyeDistance * 2) / viewNum
    rad2Deg = 180 / pi
    camAngle = math.atan2(camDist,distance)
    print camAngle
    
    for i in range(viewNum):
        #print i
        mult = (i - 4)*-1
        print mult
        objRot = c4d.Vector(camAngle * mult,0,0)
        current_object.SetRelScale(objScale)
        current_object.SetRelRot(objRot)
        current_object = current_object.GetNext()
        print current_object