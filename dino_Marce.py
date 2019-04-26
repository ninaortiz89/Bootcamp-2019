# En el archivo persona.py Crear una clase Persona con atributo nombre
# Despues instanciar un objeto de tipo persona

# Creamos una Clase Animal
class Animal:
    esta_vivo = True  # esto es un atributo de clase, dentro de los
    # metodos podemos acceder a él usano self. ej: self.esta_vivo

    def __init__(self):  # Metodo constructor, se ejecuta cuando se instancia un objeto
        pass  # en este caso no necesitamos que haga nada, por eso ponemos pass

    def morir(self):  # metodo morir que cambia el atributo de clase esta_vivo a False
        self.esta_vivo = False
        print("Me morí :( ")

# Declaramos la clase Dino que hereda los metodos y atributo de la clase Animal
class Dino(Animal):
    # patas es un atributo de clase, asignando un valor por default
    patas = 4
    # el metodo constructor __init__ recibe un nombre como parametro
    def __init__(self, un_nombre):
        # creamos el atributo de clase nombre y le asignamos el valor del argumento recibido
        self.nombre = un_nombre 
        print("Hola soy un dinosaurio, me llamo", self.nombre, "y tengo", self.patas, "patas")

    #Metodo getter para obtener el valor del atributo de calse patas
    def get_patas(self):
        return self.patas
    
    #Metodo setter para asignar el valor del atributo de clase patas
    def set_patas(self, cantidad):
        self.patas = cantidad

    # este metodo disminuye la cantidad de patas en 1 hasta que no hayan mas patas
    def cortar_pata(self):
        # disminuimos en 1 el valor del atributo de clase patas
        self.patas = self.patas - 1
        # si self.patas es menor a 1 se llama al metodo morir heredado de la clase animal
        if self.patas < 1:
            self.morir()

# Creamos/instanciamos un objeto de tipo Dino y lo guardamos en la variable pepito
pepito = Dino("Pepito")
# llamamos al metodo get_patas de la 
print(pepito.get_patas())
pepito.cortar_pata()
print(pepito.get_patas())


class TRex(Dino):
    gente_comida = 0

    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Hola soy un TRex y me llamo", self.nombre)

    def comer_gente(self, canti_gente=1):
        print("Me voy a comer", canti_gente, "persona(s)")
        self.gente_comida = self.gente_comida + canti_gente

    def __str__(self):
        return "<Objeto de tipo TRex:" + self.nombre + ">"





pepi_rex = TRex("PepitoT")
print(pepi_rex.get_patas())
pepi_rex.cortar_pata()
pepi_rex.cortar_pata()
print(pepi_rex.get_patas())
print(pepi_rex.gente_comida)
pepi_rex.comer_gente()
print(pepi_rex.gente_comida)
pepi_rex.comer_gente(5)
print(pepi_rex.gente_comida)

pepi_rex.cortar_pata()
print("canti patas:", pepi_rex.get_patas())
pepi_rex.cortar_pata()
print("canti patas:", pepi_rex.get_patas())


print("Pepi estas vivo?: ")
if pepi_rex.esta_vivo:
    print("SIIIIII")
else:
    print("...")

print(pepito)
print(pepi_rex)





