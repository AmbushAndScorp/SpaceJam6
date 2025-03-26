from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from panda3d.core import NodePath
from panda3d.core import Vec3
from CollideObjectBase import *

class Universe (InvSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, scaleVec: float):
        # setting up the universe's collision, model, scale, and texture
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), scaleVec)
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        self.modelNode.setPos(0,0,0)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)