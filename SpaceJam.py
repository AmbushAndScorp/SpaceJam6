from direct.showbase.ShowBase import ShowBase
from planets import Planet
from universe import Universe
from spaceStation import Station
from spaceship import Spaceship
from drones import Drone
import DefensePaths as DefPath
from CollideObjectBase import *
import direct.task
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib

camSwapCount = 0

class myApp(ShowBase):
    def __init__(self):
        # the base where everything is activated
        ShowBase.__init__(self)
        self.cTrav = CollisionTraverser()
        passTrav = self.cTrav
        self.SetScene(passTrav)
        self.SetCamera()
        self.CameraSwap()
        self.EnableHUD()
        fullCycle = 60
        circSpace = 0
        for j in range(fullCycle):
            # putting all the drones in place
            Drone.droneCount += 1
            nickname = "Drone" + str(Drone.droneCount)
            curCircSpace = circSpace

            self.DrawCloudDefense(self.icePlanet, nickname)
            self.DrawBaseballSeams(self.spaceStation, nickname, j, fullCycle, 2)
            self.DrawCircleX(self.redPlanet, nickname, curCircSpace)
            self.DrawCircleY(self.redPlanet, nickname, curCircSpace)
            self.DrawCircleZ(self.redPlanet, nickname, curCircSpace)
            # not too sure why X is being weird while Y and Z are working just fine, but it works so
            circSpace += 0.167

        # setting up all the collision traverser stuff
        self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.player.collisionNode, self.player.modelNode)
        self.cTrav.addCollider(self.player.collisionNode, self.pusher)
        #self.cTrav.showCollisions(self.render)
        
    # the next five put in the drone's position and where they all go in the scene
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = DefPath.BaseballSeams(step, numSeams, B=0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        Drone(self.loader, 'Assets/DroneDefender/DroneDefender.obj', self.render, droneName, 'Assets/DroneDefender/TC.jpg', position, 5)
    
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = DefPath.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        Drone(self.loader, 'Assets/DroneDefender/DroneDefender.obj', self.render, droneName, 'Assets/DroneDefender/TC.jpg', position, 10)
    
    def DrawCircleX(self, centralObject, droneName, thisCircSpace):
        unitVec = DefPath.CircleX(thisCircSpace)
        unitVec.normalize()
        position = unitVec * 200 + centralObject.modelNode.getPos()
        Drone(self.loader, 'Assets/DroneDefender/DroneDefender.obj', self.render, droneName, 'Assets/DroneDefender/TC.jpg', position, 10)
    
    def DrawCircleY(self, centralObject, droneName, thisCircSpace):
        unitVec = DefPath.CircleY(thisCircSpace)
        unitVec.normalize()
        position = unitVec * 200 + centralObject.modelNode.getPos()
        Drone(self.loader, 'Assets/DroneDefender/DroneDefender.obj', self.render, droneName, 'Assets/DroneDefender/TC.jpg', position, 10)
    
    def DrawCircleZ(self, centralObject, droneName, thisCircSpace):
        unitVec = DefPath.CircleZ(thisCircSpace)
        unitVec.normalize()
        position = unitVec * 200 + centralObject.modelNode.getPos()
        Drone(self.loader, 'Assets/DroneDefender/DroneDefender.obj', self.render, droneName, 'Assets/DroneDefender/TC.jpg', position, 10)
    
    # making sure the camera is in the right place plus some functions to swap between first and third person
    def SetCamera(self):
        self.disableMouse()
        self.camera.reparentTo(self.player.modelNode)
        self.camera.setPosHpr(Vec3(0,-20,0),Vec3(0,0,0))
    
    def CameraSwap(self):
        self.accept('r', self.Swap, [1])
    
    def Swap(self, keydown):
        global camSwapCount
        camSwapCount += 1
        if camSwapCount % 2 == 1:
            if keydown:
                self.taskMgr.add(self.FirstPerson, 'swappage')
            else:
                self.taskMgr.remove('swappage')
        else:
            if keydown:
                self.taskMgr.add(self.ThirdPerson, 'swappage')
            else:
                self.taskMgr.remove('swappage')
    
    def FirstPerson(self, task):
        self.camera.setFluidPos(0,0,0)
        return Task.cont
    
    def ThirdPerson(self, task):
        self.camera.setPosHpr(Vec3(0,-20,0),Vec3(0,1,0))
        return Task.cont
    
    # heads up display activation
    def EnableHUD(self):
        self.hud = OnscreenImage("Assets/Hud/Reticle3b.png", pos = Vec3(0,0,0), scale = 0.1)
        self.hud.setTransparency(TransparencyAttrib.MAlpha)

    # setting up the scene so everything is working
    def SetScene(self, passTrav):
        self.Universe = Universe(self.loader, "Assets/Universe/Universe.x", self.render, 'Universe', 'Assets/Universe/starfield-in-blue.jpg', 15000)

        self.icePlanet = Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, 'IcePlanet', "Assets/Planets/Ice-EQUIRECTANGULAR-2-2048x1024.png", (-6000, -3000, -800), 250)

        self.oasisPlanet = Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, 'OasisPlanet', "Assets/Planets/Oasis-EQUIRECTANGULAR-7-2048x1024.png", (0, 6000, -20), 300)

        self.primePlanet = Planet(self.loader, "Assets/Universe/Universe.x", self.render, 'PrimePlanet', "Assets/Planets/Primordial-EQUIRECTANGULAR-5-2048x1024.png", (500, -5000, 200), 300)

        self.redPlanet = Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, 'RedPlanet', "Assets/Planets/RedPlanetAnimationClouds.png", (300, 6400, 5000), 150)

        self.rockPlanet = Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, 'RockPlanet', "Assets/Planets/Rock-EQUIRECTANGULAR-15-2048x1024.png", (700, -2000, 1900), 500)

        self.savaPlanet = Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, 'SavaPlanet', "Assets/Planets/Savannah-EQUIRECTANGULAR-7-2048x1024.png", (7000, -900, -1400), 700)

        self.spaceStation = Station(self.loader, "Assets/Space Station/spaceStation.x", self.render, 'Station', "Assets/Space Station/SpaceStation1_NM.png", (1500, -100, 150), 40)

        self.player = Spaceship(passTrav, self.loader, "Assets/Spaceships/Dumbledore.egg", self.render, 'Player', "Assets/Spaceships/spacejet_N.png", (1000, 1200, -50), 50, self.taskMgr, self.accept)

app = myApp()
app.run()