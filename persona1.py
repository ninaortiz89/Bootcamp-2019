# Modificar la clase persona, agregarle un atributo edad
#  y un metodo cumple_anhos, y un metodo get_edad 
# Inicializar/crear un objeto de tipo persona y hacerle
#  cumplir anhos

class Persona: 
    nombre_persona= None
    edad= None

   
    def __init__(self, un_nombre, edad):
        self.nombre_persona= un_nombre
        self.edad= edad
        print("Hola, soy un persona y me llamo", self.nombre_persona, "mi edad es", edad)

    #def set_anhos(self, cantidad):
         #   self.anhos = cantidad
          #  self.anhos = cantidad

    def cumple_anhos(self):
        self.edad = self.edad + 1

    def get_edad (self):
        print

Luli = Persona("Luli", 16)

    
    











    
 
