from pyglet.gl import *
from pyglet.window import key

import numpy as np

BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
YELLOW  = (255,255,  0)
BLUE    = (  0,  0,255)
ORANGE  = (200,100,  0)

class Window(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        """Create pyglet window."""
        super().__init__(*args,**kwargs) #Default parameters of the pyglet window
        self.set_minimum_size(400,300) #Minimum size of the window when resizing
        self.fovy=70 #Field of view in degrees in the y direction
        self.aspect=self.width/self.height #Field of view in x direction, ration width by height, needed to get the field of view in the x direction I guess
        self.zNear=0.5 #distance of the viewer from the near clipping plane, because the camera send rays from a point and the clipping plane is a surface
        self.zFar=1000 #distance of the viewer from the far clipping plane because the rays cannot reach infinity
        self.keys = key.KeyStateHandler() #Create an object of the pyglet key type for event detection
        self.push_handlers(self.keys) #Allow automatic update of the keys of the window each turn
        self.mouse_lock=True #Lock the mouse for further player controls
        self.rubiks_cube=RubiksCube() #Rubiks cube to play with
        #pyglet.clock.schedule(self.update) #Set the clock for loop turns using pyglet update attribute
        self.player=Player((0.5,1.5,1.5),(-30,0)) #Create a player using default view parameters

    def on_draw(self): #Main draw function
        """Draw the objects of the pyglet window."""
        self.clear() #Clear the buffers
        self.set3d() #3d environment for opengl
        self.push(self.player.position,self.player.rotation) #Apply the matrix operations to set the world's position
        self.rubiks_cube.draw() #Load the matrix on the buffer
        glPopMatrix() #Pop the current matrix stack defined in the rubiks cube

    def on_mouse_motion(self,x,y,dx,dy):
        """Allow the player to change its parameters."""
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        """Allow the user to end the demonstration."""
        if KEY == key.ESCAPE: self.close()
        #elif KEY == key.E: self.mouse_lock = not self.mouse_lock
        self.mouse_lock=True #I have no idea why this thing is needed

    def Projection(self):
        """Load the projection.?"""
        glMatrixMode(GL_PROJECTION) #Allow 2 levels of depth
        glLoadIdentity() #Create the identity matrix ready to apply operations on in the push function

    def Model(self):
        """Load the model."""
        glMatrixMode(GL_MODELVIEW) #Allow any levels of depth
        glLoadIdentity() #Create the identity matrix ready to apply operations on in the push function

    def set2d(self):
        """Set a 2d environment."""
        self.Projection()
        gluOrtho2D(0,self.width,0,self.height)
        self.Model()

    def push(self,position,rotation):
        """Apply the graphical matrix operations depending on the player parameters."""
        glPushMatrix()
        glRotatef(-rotation[0],1,0,0)  #Rotate the world position according to the view of the player
        glRotatef(-rotation[1],0,1,0) #Rotate the world position according to the view of the player
        glTranslatef(-position[0],-position[1],-position[2],) #Translate the world's position from the view of the player

    def set3d(self):
        """Set a 3d environment."""
        self.Projection()
        gluPerspective(self.fovy,self.aspect,self.zNear,self.zFar) #Set the camera
        #self.Model()

    def update(self,dt):
        """Update the player's view using time dt and knowning keys."""
        self.player.update(dt,self.keys)

class RubiksCube:
    """The rubiks cube object has (n**3)-(n-2)**3 cubes."""
    def __init__(self,n=3):
        """Create a rubiks cube using n the size of the cube."""
        self.n=n #Set the size of the cube
        self.generate() #Generate the cubes of the rubiks cube
        self.batch=pyglet.graphics.Batch() #Only a single batch is created for efficiency
        self.colors=[RED,WHITE,GREEN,YELLOW,BLUE,ORANGE,BLACK]
        self.tex_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))
        #self.tex_coords = BLUE
        self.historic=[]
        self.rotating=0
        self.permutations=[]

    def generate(self):
        """Create all the outside cubes with their faces colors."""
        self.matrix=np.zeros((3,3,3,6))
        self.matrix.fill(-1)

        ld=[0,self.n-1] #List of positions along any axis
        for d in range(2): #Direction
            lc=[list(range(self.n)),list(range(self.n)),[ld[d]]] #List of colors
            for f in range(3): #Face
                m=f
                n=(m+1)%self.n
                p=(m+2)%self.n
                for z in lc[m]: #Z component
                    for y in lc[n]: #Y component
                        for x in lc[p]: #X component
                            self.matrix[x][y][z][f+3*d]=f+3*d #Color each case with the right color

    def getFace(self,n): #Useless for now
        """Extract the face number 'n'."""
        i=-1
        if n==0: return self.matrix[:][i][:] #Top face
        if n==1: return self.matrix[:][:][0] #Front face
        if n==2: return self.matrix[i][:][:] #Right face
        if n==3: return self.matrix[:][:][i] #Back face
        if n==4: return self.matrix[0][:][:] #Left face
        if n==5: return self.matrix[:][0][:] #Bottom face


    def rotate(self,n,t=1,axis=(1,0)):
        """Execute the number 'n' rotation 't' times along axis 'axis' which means it turns in counter-clockwise-direction."""
        if n==0: self.matrix[:][i][:]=np.rot90(self.matrix[:][i][:],t,axis) #Top rotation
        if n==1: self.matrix[:][:][0]=np.rot90(self.matrix[:][i][:],t,axis) #Front rotation
        if n==2: self.matrix[i][:][:]=np.rot90(self.matrix[:][i][:],t,axis) #Right rotation
        if n==3: self.matrix[:][:][i]=np.rot90(self.matrix[:][i][:],t,axis) #Back rotation
        if n==4: self.matrix[0][:][:]=np.rot90(self.matrix[:][i][:],t,axis) #Left rotation
        if n==5: self.matrix[:][0][:]=np.rot90(self.matrix[:][i][:],t,axis) #Bottom rotation

    def canCreateCube(self,x,y,z):
        """Determine if the cube can be created."""
        return (x%self.n)+(y%self.n)+(z%self.n)==0

    def drawCube(self,p1,p2,texture=None):
        """Draw a cube given its extremities."""
        x,y,z=p1
        X,Y,Z=p2
        self.batch.add(4,GL_QUADS,texture,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),self.tex_coords)
        self.batch.add(4,GL_QUADS,texture,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),self.tex_coords)
        self.batch.add(4,GL_QUADS,texture,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),self.tex_coords)
        self.batch.add(4,GL_QUADS,texture,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),self.tex_coords)
        self.batch.add(4,GL_QUADS,texture,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),self.tex_coords)
        self.batch.add(4,GL_QUADS,texture,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),self.tex_coords)


    def drawCubes(self):
        """Draw the cube at given position."""
        #Loop through the indexes to get the cubes
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    #Calculate the positions
                    p1,p2=self.getCube([x,y,z])
                    self.drawCube(p1,p2)


    def getCube(self,position,size=[1,1,1]):
        """Return the extremities of the cube defined by the given position and size."""
        offsets=[self.n/2 for i in range(3)]
        p1=[p-s/2-f for (p,s,f) in zip(position,size,offsets)]
        p2=[p-s/2+f for (p,s,f) in zip(position,size,offsets)]
        return (p1,p2)

    def draw(self):
        """Draw the batch."""
        self.drawCubes()
        self.batch.draw()

    def __str__(self):
        """Return the string representation of the object."""
        return str(self.matrix)

class Cube:
    """These cubes are the ones of the rubiks cube."""
    def __init__(self,position,size=[1,1,1],colors=[]):
        """The cubes are defined by their position."""
        self.position=position
        self.size=size
        self.colors=colors

    def rotate(self):
        """Rotate the cube."""
        #Maybe useless

    def G(self):
        """Return the point G(x,y,z) center of the cube by default."""
        return self.position

    def A(self):
        """Return the point A(xmin,ymin,zmin) by default."""
        return [p-s/2 for (p,s) in zip(self.position,self.size)]

    def B(self):
        """Return the point B(xmax,ymax,zmax) by default."""
        return [p+s/2 for (p,s) in zip(self.position,self.size)]


class Player:
    def __init__(self,position=(100,0,0),rotation=(0,0)):
        """Create a player."""
        self.position=list(position) #position of the player relative to the scene
        self.rotation=list(rotation) #rotation of the player's view relative to the scene

    def mouse_motion(self,dx,dy):
        """Allow the user to change its own view of the rubiks cube."""
        dx/=8
        dy/=8
        self.rotation[0]+=dy
        self.rotation[1]-=dx
        if self.rotation[0]>90:
            self.rotation[0]=90
        elif self.rotation[0]<-90:
            self.rotation[0]=-90

    def update(self,dt,keys):
        """Update the position of the player."""
        s=dt*10
        rotationY = -self.rotation[1]/180*math.pi #The angles are converted from degrees in radians
        dx,dz = s*math.sin(rotationY),s*math.cos(rotationY)
        if keys[key.W]: self.position[0]+=dx; self.position[2]-=dz
        if keys[key.S]: self.position[0]-=dx; self.position[2]+=dz
        if keys[key.A]: self.position[0]-=dz; self.position[2]-=dx
        if keys[key.D]: self.position[0]+=dz; self.position[2]+=dx

        if keys[key.SPACE]: self.position[1]+=s
        if keys[key.LSHIFT]: self.position[1]-=s




if __name__ == '__main__':
    window=Window(width=1440,height=900,caption='Rubiks Cube',fullscreen=False)
    r,g,b,alpha=0,0,0,1 #Color of the background and transparency alpha, each component's value must be between 0 and 1
    glClearColor(r,g,b,alpha) #Apply the background
    #glEnable allows to change the parameters of the opengl interface
    glEnable(GL_DEPTH_TEST) #Allow the objects not to be displayed when behing others, must be enabled to prevent weird bugs
    #glEnable(GL_CULL_FACE)
    pyglet.app.run()
