class InputManager:
    def __init__(self, game):
        self.game = game 
        self.keys = {
            'w': False,
            'a': False,
            's': False,
            'd': False,
            'space': False
        }
        self.key_pressed_events = {
            "space": False,
        }

        
        
        for key in self.keys:
            self.game.accept(key, self.key_pressed, [key])
            self.game.accept(f"{key}-up", self.key_up, [key])

    def key_pressed(self, key):
         self.keys[key] = True

    def key_up(self, key):
        self.keys[key] = False

    def is_key_pressed(self, key):
        return self.keys[key]

    def was_key_pressed(self, key):
        if self.key_pressed_events[key]:
            self.key_pressed_events[key] = False
            return True

    

    