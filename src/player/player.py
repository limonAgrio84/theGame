class Player:
    def __init__(self, game):
        self.game = game
        print("Player created")
        

    def update(self):
        if self.game.input_manager.is_key_pressed("w"):
            print("Moving forward")