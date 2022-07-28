class Movil():
    def __init__(self, material, estado, tiempo):
        self.material= material
        self.estado= estado
        self.tiempo= tiempo

    def __str__(self):
        info = "El movil esta hecho de {}, su estado es {} y su tiempo de vida es {}".format(self.material,self.estado,self.tiempo)
        return info 

Iphone=Movil(vidrio,nuevo,100)     