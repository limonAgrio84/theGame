from direct.showbase.ShowBase import ShowBase
from input.input_manager import InputManager
from player.player import Player

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.input_manager = InputManager(self)
        self.player = Player(self)
        #self.taskMgr.add(self.move, "Move")

    #def move(self, task):
        #if self.input_manager.is_key_pressed('w'):
            #print("Moving forward")

        #return task.cont