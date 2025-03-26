from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import *
from CollideObjectBase import *
from panda3d.core import NodePath
from panda3d.core import Vec3

class Planet (SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):\
        # setting up the planet's collision, model, position, scale, and texture
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, posVec, scaleVec + 30)
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)