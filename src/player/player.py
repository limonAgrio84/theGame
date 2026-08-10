from panda3d.core import ClockObject
from panda3d.core import Vec3
import math
class Player:
    def __init__(self, game):
        self.game = game
        print("Player created")

        self.model = self.game.loader.loadModel("models/misc/rgbCube")
        self.model.reparentTo(self.game.render)
        self.model.setScale(0.2)
        self.model.setPos(0, 10, 0)

        #velocidad
        self.speed = 5.0

        #salto
        self.vertical_velocity = 0.0
        self.gravity = 20
        self.jump_force = 8
        self.is_grounded = True



        

    def update(self):
        dt = ClockObject.getGlobalClock().getDt()

        self.move(dt)
        self.jump()

        self.apply_gravity(dt)

        

    def move(self,dt):
        direction = Vec3(0, 0, 0)

        if self.game.input_manager.is_key_pressed("w"):
                direction.y += 1
                print("Moving forward")
        
        if self.game.input_manager.is_key_pressed("s"):
            direction.y -= 1
            print("Moving backward")
        
        if self.game.input_manager.is_key_pressed('a'):
            direction.x -= 1
            print("Moving left")
        
        if self.game.input_manager.is_key_pressed('d'):
            direction.x += 1
            print("Moving right")    

        if direction.length() > 0:
             direction.normalize()

        #calcular la rotacion del modelo en base a la direccion 
        angle = math.degrees(math.atan2(direction.x, direction.y))
        self.model.setH(angle)

        #mover     
        movement = direction * self.speed * dt
        self.model.setPos(self.model.getPos() + movement)

    def jump(self):
        if self.game.input_manager.is_key_pressed("space"):
            if self.is_grounded:
                self.vertical_velocity = self.jump_force
                self.is_grounded = False

    def apply_gravity(self, dt):
        self.vertical_velocity -= self.gravity * dt

        z = self.model.getZ() 
        z += self.vertical_velocity * dt

        if z <= 0:
            z = 0
            self.vertical_velocity = 0
            self.is_grounded = True

        self.model.setZ(z)
        
        
