class Movil():
    
    def __init__(self,marca,modelo):
        self.color = "rojo"
        self.__tamaño = 15
        self.__peso = 400
        self.precio = 200
        self.__encendido = False
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        self.encendido = True
    
    def estado(self):
        if self.encendido == True:
            return("El movil esta encendido")
        else :
            return("El movil esta apagado")

    def __romper(self):  #esto es un metodo encapsulado
        pass #usando el comando pass, puedes dejar una funcion o metodo a medias,asi el pograma no dara error  

class dispositivo(Movil):
    pass 

#class zzz(Movil, dispositivo):
    #pass  #(lo de arriba) esto es una herencia multiple, el pograma posicionara la primera clase que pongamos en los parentesis, en este caso tomara los datos que se pongan hacia la clase Movil 


class marca(Movil):
    def __init__(self,fecha,marca,modelo):
        super().__init__(marca,modelo )
        self.fecha =fecha 
        self.modelo = modelo
        self.marca = marca 
    
    def estado(self):
        super().estado()
        print( "Fecha de produccion:", self.fecha)

  


samsung=marca(12,"samsung", "S22",)
samsung.estado()



