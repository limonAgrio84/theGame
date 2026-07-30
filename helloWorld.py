#from direct.showbase.ShowBase import ShowBase


#creando una clase que hereda de ShowBase, que es la clase principal de Panda3D
#class HelloWorld(ShowBase):
    #definiendo el constructor de la clase
   # def __init__(self):
        #llamando al constructor de la clase padre
   #     ShowBase.__init__(self)
        #creendo una variable que puedo usar en cualquier funcion
   #     self.count =0
    #    self.pressed_w = False

        #creando un task que se ejecutara cada frame
    #    self.taskMgr.add(self.update, "Update")

        #creando un evento con la tecla w 
     #   self.accept("w", self.w_down)
    #    self.accept("w-up", self.w_up)
     #   
        
    #definiendo el task que se ejecutara cada frame
   # def update(self, task):
   #     print(self.count)
    #    self.count += 1
    #    #esto hace que el task se ejecute cada frame, si no se retorna task.cont el task se ejecutara una sola vez
    #    #return task.cont

    #creando una funcion que se ejecutara cuando se presione la tecla w
   # def w_down(self):
   #     self.pressed_w = True
   #     print("Walking")

   # def w_up(self):
   #     self.pressed_w = False
   #     print("Stopped Walking")
#

#app = HelloWorld()
#app.run()

diccionario = {
    "w": False,
    "a": False,
    "s": False,
}

print(diccionario['w'])