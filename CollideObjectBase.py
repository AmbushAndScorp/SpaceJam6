from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):
    # the base for a placed object in the scene
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelNode: NodePath = loader.loadModel(modelPath)

        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader.loadModel(" + modelPath + ")did not return a proper PandaNode!")
        
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)

class ColliableObject(PlacedObject):
    # a base settings for making the colliders
    def __init__ (self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        super(ColliableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + '_cNode'))

class InvSphereCollideObject(ColliableObject):
    # making an inverse sphere collidier
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super(InvSphereCollideObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionInvSphere(colPositionVec, colRadius))
        #self.collisionNode.show()

class CapsoleCollisionObject(ColliableObject):
    # making a capsule collider and I know capsule is spelled wrong in the class name
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax: float, ay: float, az: float, bx: float, by: float, bz: float, r:float):
        super(CapsoleCollisionObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionCapsule(ax, ay, az, bx, by, bz, r))
        #self.collisionNode.show()

class SphereCollideObject(ColliableObject):
    # making a sphere collider
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, r: float):
        super(SphereCollideObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionSphere(colPositionVec, r))
        #self.collisionNode.show()