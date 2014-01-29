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

class model1(DirectObject):
    def __init__(self):
        self.start0=(-107.575, 17.4701, -0.65319)
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
        self.start25=(-52.7776,17.7215,0.469507)
		
       #load goose1
        self.goose1 = Actor("models/goosemodelonly",{"goose":"models/gooseanimationonly"},)      
        self.goose1.reparentTo(render)
        self.goose1.setScale(.08, .08, .08)
        self.goose1.setPos(-115.032,-34.5300,0.172455+10)
        self.goose1.setHpr(90, 0, 0)
        self.myAnimControl = self.goose1.getAnimControl("goose")
        seq1 = self.goose1.posInterval(5, Point3(-107.575, 17.4701, -0.65319+11))
        seq5 = self.goose1.posInterval(5, Point3(-124.7776,-66.7215,0.469507+10))
        seq3 = self.goose1.posInterval(5, Point3(-22.7776,17.7215,0.469507+11))
        seq2 = self.goose1.hprInterval(0, Point3(30, 0, 0), startHpr = Point3(-50, 0, 0))
        seq6 = self.goose1.hprInterval(0, Point3(90, 0, 0), startHpr = Point3(-50, 0, 0))
        
        seq4 = self.goose1.hprInterval(0, Point3(200, 0, 0), startHpr = Point3(-120, 0, 0))
        seq = Sequence(seq1, seq2, seq3, seq4, seq5, seq6)
        seq.loop()
	
	   #load penguin
        self.pingu33 = loader.loadModel("models/Penguin")      
        self.pingu33.reparentTo(render)
        self.pingu33.setScale(.4, .4, .4)
        self.pingu33.setPos(-115.032,-34.5300,0.172455)
        self.pingu33.setHpr(30, 0, 0)
        seq1 = self.pingu33.posInterval(7, Point3(-116.575, 34.4701, 0.35319))
        seq5 = self.pingu33.posInterval(7, Point3(-124.7776,-66.7215,0.469507))
        seq3 = self.pingu33.posInterval(5, Point3(-22.7776,17.7215,0.469507))
        seq2 = self.pingu33.hprInterval(0, Point3(-60, 0, 0), startHpr = Point3(-50, 0, 0))
        seq6 = self.pingu33.hprInterval(0, Point3(30, 0, 0), startHpr = Point3(-50, 0, 0))

        seq4 = self.pingu33.hprInterval(0, Point3(110, 0, 0), startHpr = Point3(-120, 0, 0))
        seq = Sequence(seq1, seq2, seq3, seq4, seq5, seq6)
        seq.loop()
	
	#skate1
        self.skate1=loader.loadModel("models/Skateboard")
        self.skate1.reparentTo(self.pingu33)
        self.skate1.setScale(.04)
	
		 #funhouse
        self.funhouse = loader.loadModel("models/funhouse")      
        self.funhouse.reparentTo(render)
        self.funhouse.setScale(.2, .2, .2)
        self.funhouse.setPos(-24,-9,1)
        self.funhouse.setHpr(100, 0, 0)
		
		
		#ringtoss
        self.ringtoss = loader.loadModel("models/ringtoss")      
        self.ringtoss.reparentTo(render)
        self.ringtoss.setScale(.2, .1, .15)
        self.ringtoss.setPos(-100, 2.8, -0.085)
        self.ringtoss.setHpr(40, 0, 0)
		
		
		#load plane
        self.plane = loader.loadModel("models/boeing707")      
        self.plane.reparentTo(render)
        self.plane.setScale(.08, .08, .08)
        self.plane.setPos(-115.032,-34.5300,0.172455+10)
        self.plane.setHpr(-125, 0, 0)
        seq1 = self.plane.posInterval(5, Point3(-100,-70,1+11))
        seq5 = self.plane.posInterval(5, Point3(-124.7776,-66.7215,0.469507+10))
        seq3 = self.plane.posInterval(10, Point3(-8.617,-45,1.2+11))
        seq2 = self.plane.hprInterval(0, Point3(-60, 0, 0), startHpr = Point3(-50, 0, 0))
        seq6 = self.plane.hprInterval(0, Point3(90, 0, 0), startHpr = Point3(-50, 0, 0))
        
        seq4 = self.plane.hprInterval(0, Point3(200, 0, 0), startHpr = Point3(-120, 0, 0))
        seq = Sequence(seq1,seq2, seq3)
        seq.loop()
	
		#collisions
		
        self.cfunhouse = self.funhouse.attachNewNode(CollisionNode('cfunhouse'))	
        self.cfunhouse.node().addSolid(CollisionSphere(0, 0, 0, 15))
        self.cpingu33 = self.pingu33.attachNewNode(CollisionNode('cpingu33'))	
        self.cpingu33.node().addSolid(CollisionSphere(0, 0, 0, 1.4))
        self.cfunhouse = self.funhouse.attachNewNode(CollisionNode('cfunhouse'))	
        self.cfunhouse.node().addSolid(CollisionSphere(0, 0, 0, 15))
        self.cringtoss = self.ringtoss.attachNewNode(CollisionNode('cringtoss'))	
        self.cringtoss.node().addSolid(CollisionSphere(0, 0, 0, 20))
       