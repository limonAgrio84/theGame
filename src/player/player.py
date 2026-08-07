class Player:
    def __init__(self, game):
        self.game = game
        print("Player created")

        self.model = self.game.loader.loadModel("models/misc/rgbCube")
        self.model.reparentTo(self.game.render)
        self.model.setScale(0.2)
        self.model.setPos(0, 10, 0)


        

    def update(self):
        if self.game.input_manager.is_key_pressed("w"):
            print("Moving forward")