#Author -Himank Shashank Saharsh
import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from pandac.PandaModules import TransparencyAttrib
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from extramodel import *
from anim import *
# width of health and stamina bars
BAR_WIDTH = 0.6

# OnscreenText to hold game timer
timeText = OnscreenText(text="0", style=1, mayChange=1,
                        fg=(1,1,1,1), pos=(1.3, -0.75), scale = .05)

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

# OnscreenText to hold number of collectibles remaining 
numObjText = OnscreenText(text="10", style=3, fg=(.1,.2,1,1),
                          pos=(.78, 0.93,0.80), scale = .1, mayChange=1)

# Ralph's health
healthBar = OnscreenImage(image="models/healthBar.png", 
                          pos=(.7, 0, 0.85), scale=(BAR_WIDTH,0.3,0.3))
healthBar.setTransparency(TransparencyAttrib.MAlpha)

# Ralph's stamina


def printNumObj(n):

    numObjText['text'] = (str)(n)

class World(DirectObject):

    def __init__(self):
        
        self.startvar=0
        self.startdialog=YesNoDialog(dialogName="START GAME", 
                                      text="START GAME" ,
                                      command=self.endbox)
        self.timepass=model()
        self.timepass1=model1() 
        self.keyMap = {"left":0, "right":0, "forward":0, "backward":0}
        base.win.setClearColor(Vec4(0,0,0,1))

        # number of collectibles
        self.numObjects = 0;
        
		#music
        self.backmusic = base.loader.loadSfx("sounds/tales.mp3")
        self.backmusic.setLoop(True)
        self.backmusic.setVolume(0.2)
        self.backmusic.play()
        
        self.skatemusic= base.loader.loadSfx("sounds/skate.mp3")
        self.skatemusic.setVolume(.65)
        self.skatemusic.setLoop(True)
		
        self.bombmusic=base.loader.loadSfx("sounds/bomb.mp3")
        self.bombmusic.setVolume(.85)
		
        self.springmusic=base.loader.loadSfx("sounds/spring.mp3")
        self.springmusic.setVolume(.65)
        self.springmusic.setLoop(True)
		
        self.colmusic=base.loader.loadSfx("sounds/collect.mp3")
        self.colmusic.setVolume(.65)
		
		
		# print the number of objects
        printNumObj(self.numObjects)

        # Post the instructions
        # self.title = addTitle("Roaming Ralph (Edited by Adam Gressen)")
        # self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        # self.inst2 = addInstructions(0.90, "[A]: Rotate Ralph Left")
        # self.inst3 = addInstructions(0.85, "[D]: Rotate Ralph Right")
        # self.inst4 = addInstructions(0.80, "[W]: Run Ralph Forward")
        # self.inst5 = addInstructions(0.75, "[S]: Run Ralph Backward")
        # self.inst6 = addInstructions(0.70, "[Space]: Run, Ralph, Run")
        
        # Set up the environment
        #
        # This environment model contains collision meshes.  If you look
        # in the egg file, you will see the following:
        #
        #    <Collide> { Polyset keep descend }
        #
        # This tag causes the following mesh to be converted to a collision
        # mesh -- a mesh which is optimized for collision, not rendering.
        # It also keeps the original mesh, so there are now two copies ---
        # one optimized for rendering, one for collisions.  

        self.environ = loader.loadModel("models/world")      
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        

        # Timer to increment in the move task
        self.time = 0
        
        # Get bounds of environment
        min, max = self.environ.getTightBounds()
        self.mapSize = max-min
        
        # Create the main character, Ralph
        self.ralphStartPos = self.environ.find("**/start_point").getPos()
        self.ralph = Actor("models/ralph",
                                 {"run":"models/ralph-run",
								  "jump":"models/ralph-jump",
                                  "walk":"models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(.30)
        self.ralph.setPos(self.ralphStartPos)
		#skate
        self.skate=loader.loadModel("models/Skateboard")
        self.skate.reparentTo(render)
        self.skate.setScale(.02)
        self.skate.setPos(-random.randint(38,50),-random.randint(15,37),-0.015)
        # ralph's health
        self.health = 100
        
		#spring
        self.spring=loader.loadModel("models/spring")
        self.spring.reparentTo(render)
        self.spring.setScale(.8)
        self.spring.setPos(-random.randint(72,78),-random.randint(10,15),6.715)
        # ralph's stamina
        self.stamina = 100
		
		
        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        
        # these don't work well in combination with the space bar
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["forward",1])
        self.accept("arrow_down", self.setKey, ["backward",1])
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["forward",0])
        self.accept("arrow_down-up", self.setKey, ["backward",0])
        
        
        
        self.accept("a", self.setKey, ["left",1])
        self.accept("d", self.setKey, ["right",1])
        self.accept("w", self.setKey, ["forward",1])
        self.accept("s", self.setKey, ["backward",1])
        self.accept("a-up", self.setKey, ["left",0])
        self.accept("d-up", self.setKey, ["right",0])
        self.accept("w-up", self.setKey, ["forward",0])
        self.accept("s-up", self.setKey, ["backward",0])

        # Game state variables
        self.isMoving = False
        self.isRunning = False
        self.onboard=0
        self.boardtime=0
        self.onspring=0
        self.isjumping = False
        # Set up the camera
        base.disableMouse()
        #base.camera.setPos(self.ralph.getX(),self.ralph.getY()+10,2)
        base.camera.setPos(0, 0, 0)
        base.camera.reparentTo(self.ralph)
        base.camera.setPos(0, 40, 2)
        base.camera.lookAt(self.ralph)
        
        # We will detect the height of the terrain by creating a collision
        # ray and casting it downward toward the terrain.  One ray will
        # start above ralph's head, and the other will start above the camera.
        # A ray may hit the terrain, or it may hit a rock or a tree.  If it
        # hits the terrain, we can detect the height.  If it hits anything
        # else, we rule that the move is illegal.

        base.cTrav = CollisionTraverser()

        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0,0,300)
        self.ralphGroundRay.setDirection(0,0,-1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.ralphGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.ralphGroundColNp = self.ralph.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()
        base.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)

        # camera ground collision handler
        self.camGroundRay = CollisionRay()
        self.camGroundRay.setOrigin(0,0,300)
        self.camGroundRay.setDirection(0,0,-1)
        self.camGroundCol = CollisionNode('camRay')
        self.camGroundCol.addSolid(self.camGroundRay)
        self.camGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.camGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.camGroundColNp = base.camera.attachNewNode(self.camGroundCol)
        self.camGroundHandler = CollisionHandlerQueue()
        base.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)

        # Place the health items
        self.placeHealthItems()
        
        # Place the collectibles
        self.placeCollectibles()
		
		# Place the bomb
        self.placebombItems()
       
        # Uncomment this line to show a visual representation of the 
        # collisions occuring
        #base.cTrav.showCollisions(render)
        
        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        #print self.startvar
        
        taskMgr.add(self.move,"moveTask")
        #taskMgr.doMethodLater(0.5, self.healthDec, "healthTask")
    
    
    # Display ralph's health
    def displayHealth(self):
        healthBar['scale'] = (self.health*0.01*BAR_WIDTH,0.2,0.2)
    
    # Display ralph's stamina
    def displayStamina(self):
        sprintBar['scale'] = (self.stamina*0.01*BAR_WIDTH,0.2,0.2)
    
    # Allow ralph to collect the health items
    def collectHealthItems(self, entry):
        # refill ralph's health
        self.colmusic.play()
        if(self.health<100):
            self.health = self.health+15.5
        # reposition the collectible
        self.placeItem(entry.getIntoNodePath().getParent())
    
    def collectCollectibles(self, entry):
        # remove the collectible
        #entry.getIntoNodePath().getParent().removeNode()
        self.colmusic.play()
        self.placeItem(entry.getIntoNodePath().getParent())
        # update the number of objects
        self.numObjects += 1
        #self.tot=10-self.numObjects
        printNumObj(self.numObjects)
		
    def blastbomb(self):
        # remove the collectible
        #self.placeItem(entry.getIntoNodePath().getParent())
        # blast 
        self.fire=loader.loadModel("models/fire")
        self.fire.reparentTo(render)
        self.fire.setScale(.01)
        self.fire.setHpr(0,-90,0)
        self.bombmusic.play()
        self.backmusic.stop()
        self.fire.setPos(self.ralph.getPos())
        self.die()
            
    # Places an item randomly on the map    
    def placeItem(self, item):
        # Add ground collision detector to the health item
        self.collectGroundRay = CollisionRay()
        self.collectGroundRay.setOrigin(0,0,300)
        self.collectGroundRay.setDirection(0,0,-1)
        self.collectGroundCol = CollisionNode('colRay')
        self.collectGroundCol.addSolid(self.collectGroundRay)
        self.collectGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.collectGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.collectGroundColNp = item.attachNewNode(self.collectGroundCol)
        self.collectGroundHandler = CollisionHandlerQueue()
        base.cTrav.addCollider(self.collectGroundColNp, self.collectGroundHandler)
        
        placed = False;
        while placed == False:
            # re-randomize position
            item.setPos(-random.randint(-40,140),-random.randint(-40,40),0)
            
            base.cTrav.traverse(render)
            
            # Get Z position from terrain collision
            entries = []
            for j in range(self.collectGroundHandler.getNumEntries()):
                entry = self.collectGroundHandler.getEntry(j)
                entries.append(entry)
            entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                         x.getSurfacePoint(render).getZ()))
        
            if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
                item.setZ(entries[0].getSurfacePoint(render).getZ()+1)
                placed = True
                
        # remove placement collider
        self.collectGroundColNp.removeNode()
    
    def placeHealthItems(self):
        self.placeholder = render.attachNewNode("HealthItem-Placeholder")
        self.placeholder.setPos(0,0,0)
        
        # Add the health items to the placeholder node
        for i in range(5):
            # Load in the health item model
            self.healthy = loader.loadModel("models/sphere")
            self.healthy.setPos(0,0,0)
            self.healthy.setScale(.4)
            self.healthy.reparentTo(self.placeholder)
            
            self.placeItem(self.healthy)
            
            # Add spherical collision detection
            healthSphere = CollisionSphere(0,0,0,1.4)
            sphereNode = CollisionNode('healthSphere')
            sphereNode.addSolid(healthSphere)
            sphereNode.setFromCollideMask(BitMask32.allOff())
            sphereNode.setIntoCollideMask(BitMask32.bit(0))
            sphereNp = self.healthy.attachNewNode(sphereNode)
            sphereColHandler = CollisionHandlerQueue()
            base.cTrav.addCollider(sphereNp, sphereColHandler)
    

#bomb
    def placebombItems(self):
        self.placebomb = render.attachNewNode("bomb-Placeholder")
        self.placebomb.setPos(0,0,0)
        
        # Add the bomb items to the placeholder node
        for i in range(30):
            # Load in the health item model
            self.bomby = loader.loadModel("models/bomb")
            self.bomby.setPos(0,0,0)
            self.bomby.setScale(.4)
            self.bomby.reparentTo(self.placebomb)
            
            self.placeItem(self.bomby)
            
            # Add spherical collision detection
            bombSphere = CollisionSphere(0,0,0,1.4)
            sphereNode = CollisionNode('bombSphere')
            sphereNode.addSolid(bombSphere)
            sphereNode.setFromCollideMask(BitMask32.allOff())
            sphereNode.setIntoCollideMask(BitMask32.bit(0))
            sphereNp = self.bomby.attachNewNode(sphereNode)
            sphereColHandler = CollisionHandlerQueue()
            base.cTrav.addCollider(sphereNp, sphereColHandler)

#blue	
    def placeCollectibles(self):
        self.placeCol = render.attachNewNode("Collectible-Placeholder")
        self.placeCol.setPos(0,0,0)
        
        # Add the health items to the placeCol node
        for i in range(50):
            # Load in the health item model
            self.collect = loader.loadModel("models/jack")
            self.collect.setPos(0,0,0)
            self.collect.setScale(.4)
            self.collect.reparentTo(self.placeCol)
            
            self.placeItem(self.collect)
            
            # Add spherical collision detection
            colSphere = CollisionSphere(0,0,0,1.4)
            sphereNode = CollisionNode('colSphere')
            sphereNode.addSolid(colSphere)
            sphereNode.setFromCollideMask(BitMask32.allOff())
            sphereNode.setIntoCollideMask(BitMask32.bit(0))
            sphereNp = self.collect.attachNewNode(sphereNode)
            sphereColHandler = CollisionHandlerQueue()
            base.cTrav.addCollider(sphereNp, sphereColHandler)
        
    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value
    
    # Makes ralph's health decrease over time
    
    
        

    
    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):   
        #print self.ralph.getPos()
        self.time += globalClock.getDt()
        timeText['text'] = str(self.time)
        
        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.
        startpos = self.ralph.getPos()
        
       

        # If a move-key is pressed, move ralph in the specified direction.
        # and rotate the camera to remain behind ralph
        if (self.keyMap["left"]!=0)and (self.onboard==0):
            self.ralph.setH(self.ralph.getH() + 100 * globalClock.getDt())
        if (self.keyMap["right"]!=0)and (self.onboard==0):
            self.ralph.setH(self.ralph.getH() - 100 * globalClock.getDt())
        if (self.keyMap["forward"]!=0)and (self.onboard==0):
            self.ralph.setY(self.ralph, -45 * globalClock.getDt())
        if (self.keyMap["backward"]!=0)and (self.onboard==0):
            self.ralph.setY(self.ralph, 45 *globalClock.getDt())
        if (self.keyMap["forward"]!=0)and (self.onboard==0) and (self.onspring>0):
		    self.ralph.setY(self.ralph, -65 * globalClock.getDt())
        if (self.keyMap["backward"]!=0)and (self.onboard==0) and (self.onspring>0):
		    self.ralph.setY(self.ralph, +65 * globalClock.getDt())


        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
        if(self.isMoving):
            if (self.health <= 0):
                self.ralph.setPos(10000,10000,1000)
                self.ralph.stop()
                self.blastbomb()
            else:
				self.health -= .07
            
        if ((self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) 
            or (self.keyMap["right"]!=0) or (self.keyMap["backward"]!=0)) and (self.onboard==0):
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving and (self.onspring==0):
                self.ralph.stop()
                self.ralph.pose("walk",5)
                self.isMoving = False
		#skate
        if(math.fabs(self.skate.getX()-self.ralph.getX())<2) and (math.fabs(self.skate.getY()-self.ralph.getY())<5) and (self.onspring==0) and (self.onboard==0):
            self.onboard=1;
            self.ralph.stop()
            self.ralph.pose("walk",5)
            self.isMoving = False
            self.isjumping = False
            self.skatemusic.play()
			
        if(self.onboard==1):
            if (self.keyMap["left"]!=0):
               self.ralph.setH(self.ralph.getH() + 60 * globalClock.getDt())
               self.skate.setH(self.ralph.getH())
            if (self.keyMap["right"]!=0):
               self.ralph.setH(self.ralph.getH() - 60 * globalClock.getDt())
               self.skate.setH(self.ralph.getH())
            if (self.keyMap["forward"]!=0):
               self.ralph.setY(self.ralph, -100 * globalClock.getDt())
               self.skate.setY(self.ralph.getY())
               self.skate.setZ(self.ralph.getZ())
               self.skate.setX(self.ralph.getX())
            if (self.keyMap["backward"]!=0):
               self.ralph.setY(self.ralph, 100 *globalClock.getDt())
               self.skate.setY(self.ralph.getY())
               self.skate.setZ(self.ralph.getZ())
               self.skate.setX(self.ralph.getX())			   
            self.boardtime=self.boardtime+1
            #self.ralph.stop()
            #self.ralph.pose("walk",5)
            #print self.onboard
            if(self.boardtime==1000):
             self.onboard=0
             self.boardtime=0
             self.skate.setPos(-random.randint(72,78),-random.randint(10,15),6.715)
             self.skatemusic.stop()
	    #spring
		#spring
        if(math.fabs(self.spring.getX()-self.ralph.getX())<2) and (math.fabs(self.spring.getY()-self.ralph.getY())<2) and(self.onboard==0)and(self.onspring==0):
            self.onspring=500
            self.springmusic.play()
            self.spring.setPos(-random.randint(38,50),-random.randint(15,37),-0.015)
			
        if (self.onspring>0):
            self.onspring=self.onspring-1
            #print self.onspring
            if (self.isjumping is False):
                self.ralph.loop("jump")
                self.isjumping = True
        else:
            #print self.ralph.getX()
            if self.isjumping:
                if((self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0)):
                    self.ralph.loop("run")
                    self.isMoving = True
                else:
                    self.ralph.stop()
                    self.ralph.pose("walk",5)
                self.isjumping = False
                self.onspring=0
                self.springmusic.stop()
				
		
        # so the following line is unnecessary
        base.cTrav.traverse(render)

        # Adjust ralph's Z coordinate.  If ralph's ray hit terrain,
        # update his Z. If it hit anything else, or didn't hit anything, put
        # him back where he was last frame.
        entries = []
        for i in range(self.ralphGroundHandler.getNumEntries()):
            entry = self.ralphGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            self.ralph.setZ(entries[0].getSurfacePoint(render).getZ())
            #base.camera.setZ(entries[0].getSurfacePoint(render).getZ()+5)
        elif (len(entries)>0) and (entries[0].getIntoNode().getName() == "healthSphere"):
            self.collectHealthItems(entries[0])
        elif (len(entries)>0) and (entries[0].getIntoNode().getName() == "colSphere"):
            self.collectCollectibles(entries[0])
        elif (len(entries)>0) and (entries[0].getIntoNode().getName() == "bombSphere"):
            self.blastbomb()
        else:
            self.ralph.setPos(startpos)
        
        # Keep the camera above the terrain
        entries = []
        for i in range(self.camGroundHandler.getNumEntries()):
            entry = self.camGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            modZ = entries[0].getSurfacePoint(render).getZ()
            base.camera.setZ(10.0+modZ+(modZ-self.ralph.getZ()))
        
        self.floater.setPos(self.ralph.getPos())
        self.floater.setZ(self.ralph.getZ()+2.0)
        base.camera.lookAt(self.floater)
        
        self.displayHealth()
        

        return task.cont
    
    #  End
    def die(self):
        # end all running tasks
        self.ralph.setPos(10000,10000,10000)
        taskMgr.remove("moveTask")
        taskMgr.remove("healthTask")
        self.ralph.stop()
        self.skatemusic.stop()
        self.springmusic.stop()
        self.backmusic.stop()
       
        colObj = self.numObjects
        myscore=str(colObj)
        
        self.highscore = OkDialog(dialogName="highscoreDialog", 
                                      text="Your Score: " + myscore,
                                      command=self.endResult)
    
    
    
    # Handle the dialog result
 
    def endResult(self, arg):
        sys.exit()
    def endbox(self,arg):
        if (arg):
            self.startvar=1
            self.startdialog.cleanup()
            # restart the game
            #self.restart()
        else:
            sys.exit() 
w = World()
run()