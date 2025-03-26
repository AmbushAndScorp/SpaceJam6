from CollideObjectBase import SphereCollideObject
from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from CollideObjectBase import *
from panda3d.core import NodePath
from panda3d.core import Vec3

class Missile(SphereCollideObject):
    # setting up the dictionaries and count for the missiles
    fireModels = {}
    cNodes = {}
    collisionSolids = {}
    Intervals = {}
    missileCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float = 1.0):
        # making the missiles have collision and the correct scale
        super(Missile, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 3.0)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setPos(posVec)

        # making sure the missile actually has collision and putting it in the right place
        Missile.missileCount += 1
        Missile.fireModels[nodeName] = self.modelNode
        Missile.cNodes[nodeName] = self.collisionNode
        Missile.collisionSolids[nodeName] = self.collisionNode.node().getSolid(0)
        Missile.cNodes[nodeName].show()
        print("Fire torpedo #" + str(Missile.missileCount))