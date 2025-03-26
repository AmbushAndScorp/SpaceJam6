from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from CollideObjectBase import *
from panda3d.core import NodePath
from panda3d.core import Vec3

class Drone(SphereCollideObject):
    # how many drones spawned
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        # setting up drone collision, model, position, scale, and texture
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 3)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)