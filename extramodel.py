import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from pandac.PandaModules import CollisionHandlerQueue, CollisionNode, CollisionSphere, CollisionTraverser
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class model(DirectObject):
    def __init__(self):
        self.start1=(-115.032,-34.5300,0.172455)
        self.start2=(-115.032-1,-34.5300-1,0.172455)
        self.start3=(-115.032+1,-34.5300-1,0.172455)
        self.start4=(-115.032+1,-34.5300-2,0.172455)
        self.start5=(-44.6318,-53.424,0.673523)
        self.start6=(-44.6318,-53.424+1,0.673523)
        self.start7=(-20.4206,-23.1125,1.58658)
        self.start8=(-20.4206+1,-23.1125+1,1.58658)
        self.start9=(-56.4692, -27.0219, -0.265594)
        self.start10=(-56.4692+1, -27.0219+1, -0.265594)
        self.start11=(-26.9805, -37.2938, 0.0976)
        self.start12=(-100.7499, -55.1375, 0.0976)
        self.start13=(-115.032,-34.5300,0.172455)
        self.start14=(-105.965,-48.3878,0.31534)
        self.start15=(-75.7024,-58.1051,0.793152)
        self.start16=(-68.9612,-27.5569,3.78519)
        self.start17=(-59.0265,-0.639381,-0.259949)
        self.start18=(-62.2102,17.403,2.02893)
        self.start19=(-16.2945,3.62409,4.32291)
        self.start20=(-54.7024,-33.1051,-0.282959)
        self.start21=(-69.7024,-10.1051,3.70898)
        self.start22=(-2.7024,3.1051,2.91034)
        self.start23=(-58.7024,-5.1051,0.0923157)
        self.start24=(-32.7776,16.7215,0.369507)
        self.start25=(-113.7776,33.3805,0.530769)	
        self.start26=(-115.7776,-1.3805,0.0366364)
        self.start27=(-88.7776,-57.3805,2.5214)
        self.start28=(-115.7776,-21.3805,0.314938)
        self.start29=(-97.7776,6.3805,0.500366)
        self.start30=(-30.7776,-13.3805,0.45137)
        self.start31=(-62.7776,-52.3805,-0.212021)
        self.start32=(-96.7776,-53.3805,0.5542068)
        self.start33=(-57.7776,9.3805,-0.165592)
		
		#load pingu1
        self.pingu1 = loader.loadModel("models/Penguin")      
        self.pingu1.reparentTo(render)
        self.pingu1.setScale(.5, .5, .5)
        self.pingu1.setPos(self.start1)
        self.pingu1.setHpr(180, 0, 0)
		
		#load pingu2
        self.pingu2 = loader.loadModel("models/Penguin")      
        self.pingu2.reparentTo(render)
        self.pingu2.setScale(.5, .5, .5)
        self.pingu2.setPos(self.start2)
        self.pingu2.setHpr(270, 0, 0)
		
		
		#load pingu3
        self.pingu3 = loader.loadModel("models/Penguin")      
        self.pingu3.reparentTo(render)
        self.pingu3.setScale(.5, .5, .5)
        self.pingu3.setPos(self.start3)
        self.pingu3.setHpr(90, 0, 0)
		
		#load pingu4
        self.pingu4 = loader.loadModel("models/Penguin")      
        self.pingu4.reparentTo(render)
        self.pingu4.setScale(.5, .5, .5)
        self.pingu4.setPos(self.start4)
        self.pingu4.setHpr(45, 0, 0)
		
		#load pingu5
        self.pingu5 = loader.loadModel("models/Penguin")      
        self.pingu5.reparentTo(render)
        self.pingu5.setScale(.5, .5, .5)
        self.pingu5.setPos(self.start10)
        self.pingu5.setHpr(270, 0, 0)
		
		#load pingu6
        self.pingu6 = loader.loadModel("models/Penguin")      
        self.pingu6.reparentTo(render)
        self.pingu6.setScale(.5, .5, .5)
        self.pingu6.setPos(self.start9)
        self.pingu6.setHpr(285, 0, 0)
		#self.myAnimControl = self.pingu6.getAnimControl('glide')
        seq1 = self.pingu6.posInterval(15, Point3(self.start1))
        seq3 = self.pingu6.posInterval(15, Point3(self.start9))
        #seq2 = self.boy.hprInterval(2, Point3(80, 0, 0), startHpr = Point3(-50, 0, 0))
        #seq4 = self.boy.hprInterval(2, Point3(-70, 0, 0), startHpr = Point3(120, 0, 0))
        seq = Sequence(seq1, seq3,)
        seq.loop()
		
		
		#Snowman1
        self.snowman1 = loader.loadModel("models/Snowman")      
        self.snowman1.reparentTo(render)
        self.snowman1.setScale(.5, .5, .5)
        self.snowman1.setPos(self.start5)
        self.snowman1.setHpr(45, 0, 0)
		
		#Snowman2
        self.snowman2 = loader.loadModel("models/Snowman")      
        self.snowman2.reparentTo(render)
        self.snowman2.setScale(.5, .5, .5)
        self.snowman2.setPos(self.start6)
        self.snowman2.setHpr(45, 0, 0)
		
		#Snowman3
        self.snowman3 = loader.loadModel("models/Snowman")      
        self.snowman3.reparentTo(render)
        self.snowman3.setScale(.5, .5, .5)
        self.snowman3.setPos(self.start7)
        self.snowman3.setHpr(45, 0, 0)
		
		#Snowman4
        self.snowman4 = loader.loadModel("models/Snowman")      
        self.snowman4.reparentTo(render)
        self.snowman4.setScale(.5, .5, .5)
        self.snowman4.setPos(self.start8)
        self.snowman4.setHpr(105, 0, 0)
		
		#snowman5
        self.snowman5 = loader.loadModel("models/Snowman")      
        self.snowman5.reparentTo(render)
        self.snowman5.setScale(.5, .5, .5)
        self.snowman5.setPos(self.start16)
        self.snowman5.setHpr(45, 0, 0)
		
		#snowman6
        self.snowman6 = loader.loadModel("models/Snowman")      
        self.snowman6.reparentTo(render)
        self.snowman6.setScale(.5, .5, .5)
        self.snowman6.setPos(self.start17)
        self.snowman6.setHpr(105, 0, 0)
		
		#snowman7
        self.snowman7 = loader.loadModel("models/Snowman")      
        self.snowman7.reparentTo(render)
        self.snowman7.setScale(.5, .5, .5)
        self.snowman7.setPos(self.start18)
        self.snowman7.setHpr(65, 0, 0)
		
		#snowman8
        self.snowman8 = loader.loadModel("models/Snowman")      
        self.snowman8.reparentTo(render)
        self.snowman8.setScale(.5, .5, .5)
        self.snowman8.setPos(self.start19)
        self.snowman8.setHpr(90, 0, 0)
		
		#snowman9
        self.snowman9 = loader.loadModel("models/Snowman")      
        self.snowman9.reparentTo(render)
        self.snowman9.setScale(.5, .5, .5)
        self.snowman9.setPos(self.start20)
        self.snowman9.setHpr(45, 0, 0)
		
		#snowman10
        self.snowman10 = loader.loadModel("models/Snowman")      
        self.snowman10.reparentTo(render)
        self.snowman10.setScale(.5, .5, .5)
        self.snowman10.setPos(self.start21)
        self.snowman10.setHpr(105, 0, 0)
		
		#snowman11
        self.snowman11 = loader.loadModel("models/Snowman")      
        self.snowman11.reparentTo(render)
        self.snowman11.setScale(.5, .5, .5)
        self.snowman11.setPos(self.start22)
        self.snowman11.setHpr(270, 0, 0)
		
		#snowman12
        self.snowman12 = loader.loadModel("models/Snowman")      
        self.snowman12.reparentTo(render)
        self.snowman12.setScale(.5, .5, .5)
        self.snowman12.setPos(self.start23)
        self.snowman12.setHpr(180, 0, 0)
		
		#snowman13
        self.snowman13 = loader.loadModel("models/Snowman")      
        self.snowman13.reparentTo(render)
        self.snowman13.setScale(.5, .5, .5)
        self.snowman13.setPos(self.start24)
        self.snowman13.setHpr(90, 0, 0)
		
		
		
		
		#farmhouse
        self.farmhouse = loader.loadModel("models/FarmHouse")      
        self.farmhouse.reparentTo(render)
        self.farmhouse.setScale(.5, .5, .5)
        self.farmhouse.setPos(self.start11)
        self.farmhouse.setHpr(105, 0, 0)
		
		#farmhouse
        self.farmhouse1 = loader.loadModel("models/FarmHouse")      
        self.farmhouse1.reparentTo(render)
        self.farmhouse1.setScale(.2, .2, .2)
        self.farmhouse1.setPos(self.start12)
        self.farmhouse1.setHpr(-25, 0, 0)
		
        #load parkfountain
        self.parkfountain = loader.loadModel("models/ParkFountain")      
        self.parkfountain.reparentTo(render)
        self.parkfountain.setScale(.5, .5, .5)
        self.parkfountain.setPos(self.start13)
        self.parkfountain.setHpr(180, 0, 0)
		
		#load parkfountain
        self.lamppost = loader.loadModel("models/LampPost")      
        self.lamppost.reparentTo(render)
        self.lamppost.setScale(.5, .5, .5)
        self.lamppost.setPos(self.start14)
        self.lamppost.setHpr(270, 0, 0)
		
		#load statue
        self.statue = loader.loadModel("models/Statue")      
        self.statue.reparentTo(render)
        self.statue.setScale(.8, .8, .8)
        self.statue.setPos(self.start15)
        self.statue.setHpr(25, 0, 0)
		
		#skate1
        self.skate=loader.loadModel("models/Skateboard")
        self.skate.reparentTo(self.pingu6)
        self.skate.setScale(.04)
        #self.skate.setPos(self.ralphStartPos.getX(),self.ralphStartPos.getY()-20,self.ralphStartPos.getZ())
		
		#load beachhouse1
        self.beachhouse = loader.loadModel("models/BeachHouse2")      
        self.beachhouse.reparentTo(render)
        self.beachhouse.setScale(.3, .3, .3)
        self.beachhouse.setPos(self.start25)
        self.beachhouse.setHpr(205, 0, 0)

		#load pb
        self.pb1 = loader.loadModel("models/ParkBench")      
        self.pb1.reparentTo(render)
        self.pb1.setScale(.2, .2, .2)
        self.pb1.setPos(self.start26)
        self.pb1.setHpr(265, 0, 0)

		#load pb
        self.pb2 = loader.loadModel("models/ParkBench")      
        self.pb2.reparentTo(render)
        self.pb2.setScale(.2, .2, .2)
        self.pb2.setPos(self.start27)
        self.pb2.setHpr(-10, 0, 0)

		#load pb
        self.pb3 = loader.loadModel("models/ParkBench")      
        self.pb3.reparentTo(render)
        self.pb3.setScale(.2, .2, .2)
        self.pb3.setPos(self.start28)
        self.pb3.setHpr(265, 0, 0)
		
		#load pb
		
        self.pb4 = loader.loadModel("models/ParkBench")      
        self.pb4.reparentTo(render)
        self.pb4.setScale(.2, .2, .2)
        self.pb4.setPos(self.start29)
        self.pb4.setHpr(85, 0, 0)
        
		#load Gazebo
		
        self.gazebo = loader.loadModel("models/Gazebo")      
        self.gazebo.reparentTo(render)
        self.gazebo.setScale(.5, .5, .5)
        self.gazebo.setPos(self.start30)
        self.gazebo.setHpr(85, 0, 0)
		
		#load Gazebo
		
        self.gazebo1 = loader.loadModel("models/Gazebo")      
        self.gazebo1.reparentTo(render)
        self.gazebo1.setScale(.5, .5, .5)
        self.gazebo1.setPos(self.start31)
        self.gazebo1.setHpr(85, 0, 0)
		
		#load car
		
        self.car = loader.loadModel("models/Car")      
        self.car.reparentTo(render)
        self.car.setScale(.2, .2, .2)
        self.car.setPos(self.start32)
        self.car.setHpr(85, 0, 0)

		#load dojo
		
        self.dojo = loader.loadModel("models/Dojo")      
        self.dojo.reparentTo(render)
        self.dojo.setScale(.02, .02, .02)
        self.dojo.setPos(self.start33)
        self.dojo.setHpr(-100, 0, 0)
		

		#Collision spheres
        self.cpingu1 = self.pingu1.attachNewNode(CollisionNode('cpingu1'))	
        self.cpingu1.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cpingu2 = self.pingu2.attachNewNode(CollisionNode('cpingu2'))	
        self.cpingu2.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cpingu3 = self.pingu3.attachNewNode(CollisionNode('cpingu3'))	
        self.cpingu3.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cpingu4 = self.pingu4.attachNewNode(CollisionNode('cpingu4'))	
        self.cpingu4.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cpingu5 = self.pingu5.attachNewNode(CollisionNode('cpingu5'))	
        self.cpingu5.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cpingu6 = self.pingu6.attachNewNode(CollisionNode('cpingu6'))	
        self.cpingu6.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.csnowman1 = self.snowman1.attachNewNode(CollisionNode('csnowman1'))	
        self.csnowman1.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman2 = self.snowman2.attachNewNode(CollisionNode('csnowman2'))	
        self.csnowman2.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman3= self.snowman3.attachNewNode(CollisionNode('csnowman3'))	
        self.csnowman3.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman4= self.snowman4.attachNewNode(CollisionNode('csnowman4'))	
        self.csnowman4.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman5 = self.snowman5.attachNewNode(CollisionNode('csnowman5'))	
        self.csnowman5.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman6 = self.snowman6.attachNewNode(CollisionNode('csnowman6'))	
        self.csnowman6.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman7 = self.snowman7.attachNewNode(CollisionNode('csnowman7'))	
        self.csnowman7.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman8 = self.snowman8.attachNewNode(CollisionNode('csnowman8'))	
        self.csnowman8.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman9 = self.snowman9.attachNewNode(CollisionNode('csnowman9'))	
        self.csnowman9.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman10 = self.snowman10.attachNewNode(CollisionNode('csnowman10'))	
        self.csnowman10.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman11 = self.snowman11.attachNewNode(CollisionNode('csnowman11'))	
        self.csnowman11.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman12 = self.snowman12.attachNewNode(CollisionNode('csnowman12'))	
        self.csnowman12.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.csnowman13 = self.snowman13.attachNewNode(CollisionNode('csnowman13'))	
        self.csnowman13.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        
        self.cfarmhouse = self.farmhouse.attachNewNode(CollisionNode('cfarmhouse'))	
        self.cfarmhouse.node().addSolid(CollisionSphere(0, 0, 0, 25))
        self.cfarmhouse1 = self.farmhouse1.attachNewNode(CollisionNode('cfarmhouse1'))	
        self.cfarmhouse1.node().addSolid(CollisionSphere(0, 0, 0, 25))	
        self.clamppost = self.lamppost.attachNewNode(CollisionNode('clamppost'))	
        self.clamppost.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cstatue = self.statue.attachNewNode(CollisionNode('cstatue'))	
        self.cstatue.node().addSolid(CollisionSphere(0, 0, 0, 2))
        self.cpb1 = self.pb1.attachNewNode(CollisionNode('cpb1'))	
        self.cpb1.node().addSolid(CollisionSphere(0, 0, 0, 5))
        self.cpb2 = self.pb2.attachNewNode(CollisionNode('cpb2'))	
        self.cpb2.node().addSolid(CollisionSphere(0, 0, 0, 5))
        self.cpb3 = self.pb3.attachNewNode(CollisionNode('cpb3'))	
        self.cpb3.node().addSolid(CollisionSphere(0, 0, 0, 5))
        self.cpb4 = self.pb4.attachNewNode(CollisionNode('cpb4'))	
        self.cpb4.node().addSolid(CollisionSphere(0, 0, 0, 5))
        self.cgazebo = self.gazebo.attachNewNode(CollisionNode('cgazebo'))	
        self.cgazebo.node().addSolid(CollisionSphere(0, 0, 0, 9))
        self.cgazebo1 = self.gazebo1.attachNewNode(CollisionNode('cgazebo1'))	
        self.cgazebo1.node().addSolid(CollisionSphere(0, 0, 0, 9))
        self.ccar = self.car.attachNewNode(CollisionNode('ccar'))	
        self.ccar.node().addSolid(CollisionSphere(0, 0, 0, 6))
        self.cdojo = self.dojo.attachNewNode(CollisionNode('cdojo'))	
        self.cdojo.node().addSolid(CollisionSphere(0, 0, 0, 250))