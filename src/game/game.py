from direct.showbase.ShowBase import ShowBase
from input.input_manager import InputManager
from player.player import Player

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        #systems
        self.input_manager = InputManager(self)
        self.player = Player(self)

        self.taskMgr.add(self.update, "Update")

    def update(self, task):
        
        self.player.update()

        return task.cont

       