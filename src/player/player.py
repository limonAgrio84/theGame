from panda3d.core import ClockObject
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


        

    def update(self):
        dt = ClockObject.getGlobalClock().getDt()

        if self.game.input_manager.is_key_pressed("w"):
            self.model.setY(self.model.getY() + self.speed * dt)
            print("Moving forward")

        if self.game.input_manager.is_key_pressed("s"):
            self.model.setY(self.model.getY() - self.speed * dt)
            print("Moving backward")

        if self.game.input_manager.is_key_pressed('a'):
            self.model.setX(self.model.getX() - self.speed * dt)
            print("Moving left")

        if self.game.input_manager.is_key_pressed('d'):
            self.model.setX(self.model.getX() + self.speed * dt)
            print("Moving right")