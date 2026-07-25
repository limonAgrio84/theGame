from direct.showbase.ShowBase import ShowBase


class HelloWorld(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #creendo una variable que puedo usar en cualquier funcion
        self.count =0

        #creando un task que se ejecutara cada frame
        self.taskMgr.add(self.update, "Update")
        
        
    #definiendo el task que se ejecutara cada frame
    def update(self, task):
        print(self.count)
        self.count += 1
        #esto hace que el task se ejecute cada frame, si no se retorna task.cont el task se ejecutara una sola vez
        return task.cont


app = HelloWorld()
app.run()